#!/usr/bin/env python

import copy
from datetime import date, datetime, timedelta
from operator import attrgetter
from os import path
import re
import sys

from pybtex.database.input import bibtex as bibtex_in
from pybtex.database.output import bibtex as bibtex_out

# error/warning display helpers
def print_error(msg):
  sys.stderr.write("[error]: " + msg + "\n")
def print_warning(msg):
  sys.stderr.write("[warning]: " + msg + "\n")
def paper_warning(paper, msg):
  if not(paper.get_id_year()) or int(paper.get_id_year()) >= 2020:
      print_warning(paper.id + ": " + msg)

# class for missing .bib field exception
class FieldError(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg

'''
Generic class containing the common fields for all papers: author, title,
abstract, project url (optional), project name (optional), author_id, and
category.
'''
class Paper(object):
  def __init__(self, id, entry):
    self.entry = entry

    # set id, author_id and category first, since they are used for
    # paper filtering
    self.id = id
 
    # set paper status
    if (id.endswith("draft")):
      self.status = "draft"
    elif (id.endswith("submission")):
      self.status = "submitted"
    else:
      self.status = "published"

    # set hidden
    self.hidden = False
    if self.type == "techreport":   self.hidden = True
    try:
      hidden_entry = entry.fields["hidden"]
      if (hidden_entry == "true"):
        self.hidden = True
      elif (hidden_entry == "false"): 
        self.hidden = False
    except KeyError: 
      pass
    if self.status != "published":  self.hidden = True

    # associate wiki names to authors
    self.add_list_field(entry, "author_id", "and")
       
    # parse the category list 
    self.add_list_field(entry, "category", ",")
    self.category = [category.lower() for category in self.category]

    # parse the fields common to conference papers, journal papers, and
    # technical reports
    try:
      self.author = entry.persons["author"]
    except KeyError: 
      raise FieldError("missing " + author + " field")
    if (len(self.author) != len(self.author_id)):
      err_msg = "<" + self.id + "> " + "item count mismatch: " \
              + str(len(self.author)) + " items in field " + "author" + " vs " \
              + str(len(self.author_id)) + " items in field " + "author_id"
      raise FieldError(err_msg)

    self.add_field(entry, "title")
    self.add_field(entry, "abstract")
    self.add_optional_field(entry, "project_url", warning=True)
    self.add_optional_field(entry, "project_name", default="project")

    # set date
    # set month
    try:
      mm = datetime.strptime(entry.fields["month"], "%B").month
    except ValueError:
      try:
        mm = datetime.strptime(entry.fields["month"], "%b").month
      except ValueError:
        paper_warning(self, "invalid month " + entry.fields["month"] )
        mm = 1
    except KeyError:
      mm = 1

    # set year
    try:
      yyyy = int(entry.fields["year"][0:4])
    except ValueError:
      print_error("<" + self.id + "> " + "invalid year " + entry.fields["year"])
      yyyy = 1900
      print("===", self.get_id_year())
    except KeyError:
      yyyy = self.get_id_year()

    self.date = date(yyyy, mm, 1)

    # set to appear status
    try:
      to_appear_entry = entry.fields["to_appear"]
      if (to_appear_entry == "true"):
        self.to_appear = True
      elif (to_appear_entry == "false"): 
        self.to_appear = False
    except KeyError: 
      if (self.status == "published" and self.type != "techreport"
          and not isinstance(self, Thesis)):
        self.to_appear = not ("doi" in entry.fields or "pages" in entry.fields)
      else:
        self.to_appear = False

  def add_field(self, entry, name):
    try:
      setattr(self, name, entry.fields[name])
    except KeyError:
      raise FieldError("<" + self.id + "> " + "missing " + name + " field")

  def add_optional_field(self, entry, name, default="", warning=False):
    flag = True
    try:
      value = entry.fields[name]
    except KeyError: 
      value = default
      flag = False
      if (warning):
        paper_warning(self, "missing " + name + " field")
    setattr(self, name, value)
    return flag

  def add_list_field(self, entry, name, sep):
    try:
      content = entry.fields[name]
    except KeyError: 
      raise FieldError("<" + self.id + "> " + "missing " + name + " field")

    if (sep != ""):
      if (sep[0].isalnum()):
        sep = "\s+" + sep
      else:
        sep = "\s*" + sep
      if (sep[-1].isalnum()):
        sep = sep + "\s+"
      else:
        sep = sep + "\s*"
    else:
      sep = "\s+"

    list = re.split(sep, content.strip())
    setattr(self, name, list)

  def get_title(self):
    return "name=" + self.title.replace("{", "").replace("}", "")

  def get_authors(self):
    #author_wikilink_list = ["[[" + id + "]]" for id in self.author_id]
    author_wikilink_list = [Paper.get_author_link(id) for id in self.author_id]
    authors = "authors=" + " and ".join(author_wikilink_list)

    return authors

  @staticmethod
  def get_author_link(id):
    if (id.startswith("http")):
      return "[" + id + "]"
    else:
      return "[[" + id + "]]"

  def get_abstract(self):
    return "abstract=" + self.abstract

  def get_wiki_content(self):
    if (self.hidden):
      return None

    wiki_content = "{{" + args.template \
                 + "|" + self.get_title() \
                 + "|" + self.get_authors() \
                 + "|" + self.get_details() \
                 + "|" + self.get_abstract() \
                 + "|" + self.get_links() \
                 + "}}"

    return wiki_content

  def get_details(self):
    details = "details=" + self.get_new() + " " + self.get_details_content()
    if (self.to_appear):
      details += ". To appear"

    return details

  @staticmethod
  def get_link_helper(url, name):
    if (url == None or url == ""):
      return None;
    else:
      return url + " " + name

  @staticmethod
  def get_links_helper(link_list):
    # filter the list of empty links (generated by optional fields)
    link_list = ["[" + link + "]" for link in link_list if link != None]
    links = "links=" + ", ".join(link_list)

    return links

  def get_pdf_link(self):
    return Paper.get_link_helper(self.public_pdf, "PDF")
 
  def get_project_link(self):
    return Paper.get_link_helper(self.project_url, self.project_name)

  def get_doi_link(self):
    doi = getattr(self, "doi", "")
    return Paper.get_link_helper(doi, "DOI")

  #def get_svn_link(self):
  #  if (args.private):
  #    svn = self.paper_svn
  #  else:
  #    svn = ""
  #  return Paper.get_link_helper(svn, "SVN")

  def get_reviews_link(self):
    if (args.private):
      reviews = self.reviews
    else:
      reviews = "" 
    return Paper.get_link_helper(reviews, "Reviews")

  def get_bib_link(self):
    return Paper.get_link_helper(self.bib, "BIB")

  def get_id_year(self):
    items = self.id.split("-")
    try:
      if (items[len(items) - 1] == "draft"
          or items[len(items) - 1] == "submission"):
        yyyy = items[len(items) - 3]
      else:
        yyyy = items[len(items) - 2]
 
      return int(yyyy)
    except:
      print_error("<" + self.id + "> " + "unexpected format of paper id ")
      return 1900

  def get_new(self):
    new_string = "NEWENTRY"
    # drafts and submissions are never new
    if (self.status != "published"):
      return ""
    # "to appear" papers are always new
    if (self.to_appear):
      return new_string
    # published papers are new 90 days after the publication month
    if (date.today() < self.date + timedelta(days=90)):
      return new_string
    else:
      return ""


'''
Class containing specific conference paper fields. Extends Paper.
'''
class ConferencePaper(Paper):
  type = "inproceedings"

  def __init__(self, id, entry):
    Paper.__init__(self, id, entry)
    
    if (self.status == "draft"):
      return

    # fields for submitted conference papers
    self.add_field(entry, "booktitle_acronym")
    self.add_optional_field(entry, "booktitle_url", warning=True)

    if (self.status == "submitted"):
      return

    # fields for conference papers accepted for publication
    self.add_field(entry, "booktitle")

    try:
      # series_acronym field supersedes publisher field
      # self.publisher = entry.fields["series"]
      self.publisher = entry.fields["series_acronym"]
    except KeyError: 
      try:
        # default to series field
        self.publisher = entry.fields["series"]
      except KeyError:
        try: 
          # default to publisher
          self.publisher = entry.fields["publisher"]
        except KeyError:
          # unknown publisher
          self.publisher = ""
          paper_warning(self, "missing publisher/series" + " field")
    # warning for unusual publisher/series
    # if (self.publisher != ""
    #    and self.publisher != "ACM"
    #    and self.publisher != "IEEE"
    #    and self.publisher != "LNCS"
    #    and self.publisher != "ENTCS"):
    #  paper_warning(self,   "unrecognised publisher/series " 
    #                + self.publisher)
    self.add_optional_field(entry, "volume")
    # warning for LNCS/ENTCS with no volume info
    if (self.publisher == "LNCS" or self.publisher == "ENTCS"):
      if (self.volume == ""):
        paper_warning(self, "missing volume information for LNCS/ENTCS publication")
    has_field = self.add_optional_field(entry, "pages", warning=True)
    #check the format of the content of pages
    if (has_field == True):
      if (self.pages != "---"):
        if (self.pages != ""):
          pattern = re.compile(r'([0-9]+)(\-)([0-9]+)')
          match = pattern.match(self.pages)
          if not match:
            paper_warning(self,  "The format of pages \""  + self.pages + "\" is not correct")
        else:
          paper_warning(self, "missing pages content")
      else:
        self.pages = ""

    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)

    self.add_field(entry, "year")

    self.add_optional_field(entry, "doi", warning=True)

    self.add_optional_field(entry, "presentation_url")
    if (self.presentation_url == ""):
      self.add_optional_field(entry, "presentation", warning=True)

  def get_details_content(self):
    details = ""
    if (self.status == "draft"):
      details += "draft"
      return details

    if (self.status == "submitted"):
      details += "submitted to " + self.booktitle_acronym
      return details

    details += "'''''" + self.booktitle_acronym + "'''''"
    if (self.publisher != ""):
      details += ", " + self.publisher
      if (self.volume != ""):
        details += " " + self.volume 
    if (self.pages != ""):
      details += ", " + "pp " + self.pages
    details += ". "
    details += self.year
   
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.extend(self.get_presentation_links())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    link_list.append(self.get_booktitle_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_reviews_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 

  def get_presentation_links(self):
    if (self.status != "published"):
      return []

    if (self.presentation_url != ""):
      return [Paper.get_link_helper(self.presentation_url, "Slides")]

    if (self.presentation == ""):
      return []

    prefix = path.join(self.presentation_dir, self.presentation)
    prefix_www = self.presentation_www + "/" + self.presentation

    presentation_links = [
        Paper.get_link_helper(
            prefix_www + "." + ext,
            "Slides(" + ext.upper() + ")")
        for ext in ["pptx", "ppt", "key", "pdf"]
        if path.isfile(prefix + "." + ext)]
    
    if (presentation_links == []):
      paper_warning(self,   "no presentation found")

    return presentation_links

  def get_booktitle_link(self):
    try:
      return Paper.get_link_helper(self.booktitle_url, self.booktitle_acronym)
    except AttributeError:
      return None 


'''
Class containing specific journal paper fields. Extends Paper.
'''
class JournalPaper(Paper):
  type = "article"

  def __init__(self, id, entry):
    Paper.__init__(self, id, entry)

    if (self.status == "draft"):
      return

    # fields for submitted journal papers
    self.add_field(entry, "journal_acronym")
    self.add_field(entry, "journal_url")

    if (self.status == "submitted"):
      self.add_optional_field(entry, "year", warning=False)
      return

    # fields for journal papers accepted for publication
    self.add_field(entry, "journal")
    self.add_optional_field(entry, "volume", warning=True)
    self.add_optional_field(entry, "number", warning=True)
    has_field = self.add_optional_field(entry, "pages", warning=True)
    
    if (has_field == True):
      if (self.pages != "---"):
        if (self.pages != ""):
          pattern = re.compile(r'([0-9]+)(\-)([0-9]+)')
          match = pattern.match(self.pages)
          if not match:
            paper_warning(self,   "The format of pages \""
                        + self.pages + "\" is not correct")
        else:
          paper_warning(self, "missing pages content")
      else:
        self.pages = ""


    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_optional_field(entry, "doi", warning=True)

  def get_details_content(self):
    details = ""

    #details for draft
    if (self.status == "draft"):
      details += "draft"
      return details

    #details for submitted
    if (self.status == "submitted"):
      details += "submitted to " + self.journal_acronym
      if (self.year != ""):
        details += ". " + self.year
      return details

    details += "'''''" + self.journal_acronym + "'''''"
    if (self.volume != ""):
      details += ", " + "Volume" + " " + self.volume 
    if (self.number != ""):
      details += "(" + self.number + ")"
    if (self.pages != ""):
      details += ", " + "pp " + self.pages
    details += ". " + self.year

    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    link_list.append(self.get_journal_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_reviews_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 

  def get_journal_link(self):
    try:
      return Paper.get_link_helper(self.journal_url, self.journal_acronym)
    except AttributeError:
      return None 


'''
Class containing specific technical report fields. Extends Paper.
'''
class TechnicalReport(Paper):
  type = "techreport"

  def __init__(self, id, entry):
    Paper.__init__(self, id, entry)

    # fields for published technical reports
    self.add_field(entry, "institution")
    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_field(entry, "number")
    self.add_optional_field(entry, "doi", default=self.number)

  def get_details_content(self):
    details = "'''''" + "Technical Report" + "'''''"

    # the following 3 cases should not occur
    if (self.status != "published"):
      return details

    details += " " + self.number + ", "
    details += self.month + " " + self.year
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 


'''
Class containing specific thesis fields. Extends Paper.
'''
class Thesis(Paper):

  def __init__(self, id, entry):
    Paper.__init__(self, id, entry)

    # fields for published technical reports
    self.add_field(entry, "school")
    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_optional_field(entry, "doi", warning=True)

  def get_details_content(self):
    details = "'''''" + self.display_thesis_type + "'''''"

    # the following 3 cases should not occur
    if (self.status != "published"):
      return details

    details += ", " + self.school + ". "
    details += self.month + " " + self.year
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list)


'''
Class containing specific master thesis fields. Extends Thesis.
'''
class MasterThesis(Thesis):
  type = "mastersthesis"
  display_thesis_type = "Master's Thesis"

  def __init__(self, id, entry):
    Thesis.__init__(self, id, entry)


'''
Class containing specific phd thesis fields. Extends Thesis.
'''
class PhDThesis(Thesis):
  type = "phdthesis"
  display_thesis_type = "PhD Thesis"

  def __init__(self, id, entry):
    Thesis.__init__(self, id, entry)


### Data used for the report

* Data used in the report is collected from the [GitHub API](https://developer.github.com/v3/).
* Accuracy of the data and conclusions drawn from it, depends directly on API results.

---

### Organization account verification on GitHub

* Organization accounts used in the report are not verified by any authorities.
* They were verified just on the basis of Name, Service/Blog URL, Email etc.
* They may represent some non-original organizations, in case of any mistake.

---

### GitHub organization creation date of organizations

* GitHub organization's creation date is [provided](https://developer.github.com/v3/orgs/#get-an-organization) by GitHub API itself.
* Subject to the name/handle of the organization.

---

### Public lanunching date of Organizations

* Public launching dates of organizations was collected from different sources like Crunchbase, WikiPedia, Google, Twitter or Organization's blog/about pages.
* In some cases where the exact date was not available, it was assumed as 15th of the month.

---

### Stars Distribution

* No. of stars for each repository are not updated in real-time.
* Stars used for the conclusions are from the time of data collection.

---

### Timeline Activity

* For a *source* repository, all its commits were counted as it is.
* For a *forked* repository, all the commits after the fork date are counted.
* Code for this filteration is available here, [timeline.py#L67-L98](https://github.com/pravj/ospi/blob/master/collector/timeline.py#L67-L98).

---

### Active and Inactive fork attributes

* This was decided from the [timeline activity](https://github.com/pravj/ospi/blob/master/data/timeline.csv) and [Forked repository status](https://github.com/pravj/ospi/blob/master/data/forked_repo_stats.csv) data.
* All the forked repositories that have 0 commit activities in the last year, according to the timeline activity data, are considered as *inactive-forked*.
* The code for this is available here, [repository-attribute.R#L19-L21](https://github.com/pravj/ospi/blob/master/R/repository-attribute.R#L19-L21).

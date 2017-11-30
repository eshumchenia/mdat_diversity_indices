Comparing MDAT diversity metrics
================
emily shumchenia
30 November 2017

Take-home message
-----------------

> If you are concerned about accounting for and considering rare species, **SPECIES RICHNESS** does the best job, by representing every species equally, regardless of abundance
>
> If you care about rare species, but need to give some additional consideration to species that are particularly abundant, the **SHANNON INDEX** does a good job
>
> If abundant or dominant species are important for your analysis, the **SIMPSON INDEX** gives more weight to highly abundant species, to the detriment of the representation of the rarest species
>
> **EACH DIVERSITY METRIC** may respond differently to ecological features. If you care about a specific habitat type or ecological component, you may want to examine the behavior of all three metrics to help select the most responsive measure.

Introduction
------------

What are diversity metrics?

When most people think about diversity, they think about the total number of species in an area. However, the total number of species is actually a metric called Species Richness.

Diversity indices take the total number of species *and* their abundances into account (in different ways, depending on the index).

Because each metric integrates information differently, it is important to know how they are similar or different, and how the outputs could be used.

Purpose
-------

MDAT has represented diversity with three different metrics: Species Richness, the Shannon Index, and the Simpson Index. The purpose of this document is to explore a few questions about these metrics:

1.  Are the metrics similar or different?
2.  How do their results compare to one another?
3.  Do the metrics represent ecological patterns similarly?

Below are maps (top row) and histograms (bottom row) for Species Richness, Shannon Diversity, and Simpson Diversity for all cetacean species:

![](div_indices_files/figure-markdown_github-ascii_identifiers/maps-1.png)

QUESTION: Are the metrics similar or different?
-----------------------------------------------

ANSWER: From the maps and histograms we can tell that Shannon and Simpson are more similar to each other than either of them are to Species Richness. We can check this by doing a simple correlation between each pair of metrics:

|          |  richness|  simpson|  shannon|
|----------|---------:|--------:|--------:|
| richness |      1.00|     0.49|     0.56|
| simpson  |      0.49|     1.00|     0.96|
| shannon  |      0.56|     0.96|     1.00|

This result is not surprising since both Shannon and Simpson indices consider abundance information, and Species Richness does not.

QUESTION: How do the metrics' results compare to one another?
-------------------------------------------------------------

We know that results for Species Richness are quite different from both Shannon and Simpson results. To understand differences in the results of these two indices (how each deals differenetly with abundance information), we can plot the Shannon and Simpson results together. The plot below shows how abundance information at each location has contributed to each diversity index value for that location:

\[insert plot from Jesse\]

ANSWER: This plot shows that for low to medium abundance values, both the Shannon Index and Simpson index generate comparable diversity results. However, for high abundance values, the Simpson index generates a proportionally much higher diversity value than the Shannon index.

This result indicates that the Simpson index gives more weight to highly abundant species than the Shannon index. The Shannon index treats rare species and dominant species more equally.

QUESTION: Do the metrics represent ecological patterns similarly?
-----------------------------------------------------------------

We know that depth is an important habitat variable for cetaceans - certain groups of species spend more time in deeper water, while other species have more coastal distributions.

So, does each metric represent cetacean diversity similarly across different ocean habitats? In other words, will each metric give us the same answer to the question: "how does cetacean diversity respond to depth?"

A linear regression of each diveristy metric on water depth will help explain whether the three metrics respond similarly to real changes in cetacean diversity that may occur with depth.

![](div_indices_files/figure-markdown_github-ascii_identifiers/regression_results-1.png)

ANSWER: While the general response of each metric to depth is similar (all show increasing diversity with depth), the strength of each relationship is different. In this case, Species Richness is most responsive to changes in depth.

Comparing MDAT diversity metrics
================
emily shumchenia
30 November 2017

Purpose
-------

The purpose of this document is to explore the similarities and differences among the three diversity metrics calculated for MDAT products, and what those might mean ecologically.

We'll be looking at Species Richness, Shannon Diversity, and Simpson Diversity for all cetacean species:

![](div_indices_files/figure-markdown_github-ascii_identifiers/maps-1.png)

Quick comparison
----------------

From the maps we can tell that Shannon and Simpson are more similar to each other than either of them are to Species Richness. We can check this by doing a simple correlation between each pair of metrics:

|          |  richness|  simpson|  shannon|
|----------|---------:|--------:|--------:|
| richness |      1.00|     0.49|     0.56|
| simpson  |      0.49|     1.00|     0.96|
| shannon  |      0.56|     0.96|     1.00|

Ecological relationships
------------------------

Which diversity metric can best discriminate between different ocean habitats? Knowing which metric is best could help users choose which metric to use in spatial planning decisions. An important cetacean habitat variable is depth. A linear regression of each diveristy metric on water depth can help determine which metric most strongly shows this association.

![](div_indices_files/figure-markdown_github-ascii_identifiers/regresion%20results-1.png)
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Linear regression with depth
</caption>
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:right;">
r
</th>
<th style="text-align:right;">
p
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
richness
</td>
<td style="text-align:right;">
0.41
</td>
<td style="text-align:right;">
0.001
</td>
</tr>
<tr>
<td style="text-align:left;">
shannon
</td>
<td style="text-align:right;">
0.29
</td>
<td style="text-align:right;">
0.001
</td>
</tr>
<tr>
<td style="text-align:left;">
simpson
</td>
<td style="text-align:right;">
0.19
</td>
<td style="text-align:right;">
0.001
</td>
</tr>
</tbody>
</table>

---
title: "MapUpdaterMapUpdateVersionCommitPolicy enum"
slug: "sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdaterMapUpdateVersionCommitPolicy.html -->


<div>
<h1>MapUpdaterMapUpdateVersionCommitPolicy enum</h1>
</div>

<p>Defines if installed regions and subregions are updated one-by-one or if all regions are
updated only once the updates for all installed regions have been downloaded entirely.</p>
<p>This influences the required size of the storage during an update.
Regardless of the set policy, during an update, the previous region data is kept
until the new region data is committed successfully to the persisted storage.
This allows to revert to the previous version in case the update fails.
With <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onComplete</a>, more data has to be kept until
the update process finishes, while <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a>
allows to make faster use of the downloaded region and requires less disk space as only the
currently updated region is kept until the process completes.
However, with an <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a> policy the overall
process can be less reliable and bears a higher risk of errors.</p>


<h2>Values</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-index">index</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-operator-equals">operator ==</a></li></ul>


<h2>Constants</h2>
<ul><li><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-values-constant">values</a></li></ul>





</div>
`
}</HTMLBlock>

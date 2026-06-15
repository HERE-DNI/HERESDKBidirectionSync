---
title: "version property"
slug: "sdk-for-flutter-explore-core-engine-catalogidentifier-version"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- version.html -->


<div>
<h1>version property</h1></div>

        
        int?
        version
<div class="features">getter/setter pair</div>


<p>A version number for a catalog. When accessing a catalog, this version must be specified.
Set <code>null</code> to automatically get the latest version for a catalog.
The field defaults to <code>null</code>.
Since the data inside a catalog can be updated, each published modification needs to correlate
to a specific version number.
Note: when <code>CatalogIdentifier</code> created with <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a> then:</p>
<ul>
<li>numerical <code>-1</code> corresponds to <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> with <code>ignoreCachedData</code> set to <code>true</code>;</li>
<li><code>null</code> corresponds to <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> with <code>ignoreCachedData</code> set to <code>false</code>;</li>
<li>other numerical values correspond to <code>version</code> passed to <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? version;</code></pre>

 



</div>
`
}</HTMLBlock>

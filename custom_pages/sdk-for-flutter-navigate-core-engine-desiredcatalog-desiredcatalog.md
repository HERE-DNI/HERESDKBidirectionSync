---
title: "DesiredCatalog constructor"
slug: "sdk-for-flutter-navigate-core-engine-desiredcatalog-desiredcatalog"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DesiredCatalog.html -->


<div>
<h1>DesiredCatalog constructor</h1></div>

DesiredCatalog(<ol class="parameter-list single-line"> <li>String hrn, </li>
<li><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a> version</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li>
<p><code>hrn</code> A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
catalog to your project. For more information, see <a href="sdk-for-flutter-navigate-core-engine-catalogidentifier-hrn">CatalogIdentifier.hrn</a></p>
</li>
<li>
<p><code>version</code> The version to use for this Catalog's data.
You should use either <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a> to specify a specific version of the catalog or
<a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> to access the latest version of the catalog available on the HERE platform.
Based on the value in this field, the HERE platform will determine the best version to use for this catalog
or result in error logs if the desired version is not available.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DesiredCatalog(String hrn, CatalogVersionHint version) =&gt; $prototype.make(hrn, version);</code></pre>

 



</div>
`
}</HTMLBlock>

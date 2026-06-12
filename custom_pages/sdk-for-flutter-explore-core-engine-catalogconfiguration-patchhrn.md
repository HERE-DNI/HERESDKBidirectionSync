---
title: "patchHrn property"
slug: "sdk-for-flutter-explore-core-engine-catalogconfiguration-patchhrn"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- patchHrn.html -->


<div>
<h1>patchHrn property</h1></div>

        
        String?
        patchHrn
<div class="features">getter/setter pair</div>


<p>Some catalogs may have additional modifications to their data
contained in an entirely separate catalog, called the patch catalog.
This field indicates the HERE Resource Name (HRN) for the patch catalog.
When this field is present, the catalog's data as referenced by
<a href="/sdk-for-flutter-explore-core-engine-catalogconfiguration-catalog">CatalogConfiguration.catalog</a> is merged with data from the patch catalog.
If this field is <code>null</code>, then incremental updates are disabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? patchHrn;</code></pre>

 



</div>
`
}</HTMLBlock>

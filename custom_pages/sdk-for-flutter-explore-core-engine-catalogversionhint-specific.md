---
title: "specific static method"
slug: "sdk-for-flutter-explore-core-engine-catalogversionhint-specific"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- specific.html -->


<div>
<h1>specific static method</h1></div>

<a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a>
specific(<ol class="parameter-list single-line"> <li>int version</li>
</ol>)

      

    

<p>This static method is used when you are interested in a
specific version of a catalog, that you want to specify manually.</p>
<p>To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.</p>
<ul>
<li><code>version</code> An integer value indicating the version of catalog desired.
If the desired version does not exist, the HERE platform will make the
best effort to provide an appropriate version or result in error logs
about invalid version.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a>. Instance of <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a> with specified version.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static CatalogVersionHint specific(int version) =&gt; $prototype.specific(version);</code></pre>

 



</div>
`
}</HTMLBlock>

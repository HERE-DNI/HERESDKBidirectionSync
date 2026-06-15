---
title: "RasterDataSourceConfiguration constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-rasterdatasourceconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceConfiguration.html -->


<div>
<h1>RasterDataSourceConfiguration constructor</h1></div>

RasterDataSourceConfiguration(<ol class="parameter-list"> <li>String name, </li>
<li><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class">RasterDataSourceProviderConfiguration</a> provider, </li>
<li><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class">RasterDataSourceCacheConfiguration</a> cache, </li>
<li>bool ignoreExpiredData, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>name</code> The unique name of the data source.</li>
<li><code>provider</code> Data provider configuration.</li>
<li><code>cache</code> Local cache configuration.</li>
<li><code>ignoreExpiredData</code> A flag indicating whether expired data should be ignored until refreshed. Default value is <code>false</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceConfiguration(this.name, this.provider, this.cache, this.ignoreExpiredData);</code></pre>

 



</div>
`
}</HTMLBlock>

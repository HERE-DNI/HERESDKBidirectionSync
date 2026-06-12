---
title: "RasterDataSourceConfigurationUpdate constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfigurationupdate-rasterdatasourceconfigurationupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceConfigurationUpdate.html -->


<div>
<h1>RasterDataSourceConfigurationUpdate constructor</h1></div>

RasterDataSourceConfigurationUpdate(<ol class="parameter-list single-line"> <li>Map&lt;String, String&gt;? providerHeaders, </li>
<li>bool? ignoreExpiredData, </li>
<li>int? cacheDiskSize</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>providerHeaders</code> Optional update of the provider headers. The new list replaces the current one.
When not set, no change is made to the current list.</li>
<li><code>ignoreExpiredData</code> Optional update of the flag indicating whether expired data should be ignored until refreshed.
When not set, no change is made to the current flag state.</li>
<li><code>cacheDiskSize</code> Optional update of the cache disk size, in bytes.
When not set, no change is made to the current value.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceConfigurationUpdate(this.providerHeaders, this.ignoreExpiredData, this.cacheDiskSize);</code></pre>

 



</div>
`
}</HTMLBlock>

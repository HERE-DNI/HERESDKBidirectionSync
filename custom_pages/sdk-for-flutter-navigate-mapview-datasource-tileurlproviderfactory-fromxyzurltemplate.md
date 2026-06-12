---
title: "fromXyzUrlTemplate static method"
slug: "sdk-for-flutter-navigate-mapview-datasource-tileurlproviderfactory-fromxyzurltemplate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromXyzUrlTemplate.html -->


<div>
<h1>fromXyzUrlTemplate static method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a>?
fromXyzUrlTemplate(<ol class="parameter-list single-line"> <li>String urlTemplate</li>
</ol>)

      

    

<p>Creates <a href="/sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a> for the given URL template.</p>
<p>A url template should look like this 'https://TestRasterTileService.com/{z}/{x}/{y}/'
here the z parameter is the storage level, x and y define the location of the tile.
The valid range for X and Y is from 0 to 2^level − 1.</p>
<ul>
<li><code>urlTemplate</code> The url template</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback?</a>. <code>null</code> if the provided template is not valid xyz url type.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static TileUrlProviderCallback? fromXyzUrlTemplate(String urlTemplate) =&gt; $prototype.fromXyzUrlTemplate(urlTemplate);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "TileSourceDataVersion constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-tilesourcedataversion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileSourceDataVersion.html -->


<div>
<h1>TileSourceDataVersion constructor</h1></div>

TileSourceDataVersion(<ol class="parameter-list single-line"> <li>int majorVersion, </li>
<li>int minorVersion</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>majorVersion</code> Major version number.
Describes changes in underlying data that would require a complete reload
(e.g. geometry changes).</li>
<li><code>minorVersion</code> Minor version number.
Describes changes in underlying data that would not require a complete reload
(e.g. attributes changes).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TileSourceDataVersion(this.majorVersion, this.minorVersion);</code></pre>

 



</div>
`
}</HTMLBlock>

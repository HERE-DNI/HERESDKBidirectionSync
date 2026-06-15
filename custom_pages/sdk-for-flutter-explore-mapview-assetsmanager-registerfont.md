---
title: "registerFont abstract method"
slug: "sdk-for-flutter-explore-mapview-assetsmanager-registerfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- registerFont.html -->


<div>
<h1>registerFont abstract method</h1></div>

void
registerFont(<ol class="parameter-list single-line"> <li>String fontName, </li>
<li>String fontPath</li>
</ol>)

      

    

<p>Registers a font under a font name.</p>
<p>After registration, the font name can be used in</p>
<ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> with <code>ImageFormat.SVG</code>.</li>
<li><a href="sdk-for-flutter-explore-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a></li>
</ul>
<p>Repeated registration with the same font name is ignored.</p>
<ul>
<li>
<p><code>fontName</code> A font name.</p>
</li>
<li>
<p><code>fontPath</code> A font file path. TTF, OTF and WOFF formats are supported.</p>
</li>
</ul>
<p>Can be an asset file path or an absolute file path.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void registerFont(String fontName, String fontPath);</code></pre>

 



</div>
`
}</HTMLBlock>

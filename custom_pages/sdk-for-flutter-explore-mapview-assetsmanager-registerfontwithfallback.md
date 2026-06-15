---
title: "registerFontWithFallback abstract method"
slug: "sdk-for-flutter-explore-mapview-assetsmanager-registerfontwithfallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- registerFontWithFallback.html -->


<div>
<h1>registerFontWithFallback abstract method</h1></div>

void
registerFontWithFallback(<ol class="parameter-list single-line"> <li>String fontName, </li>
<li>String fontPath, </li>
<li>List&lt;String&gt; fallbackFontFilePaths</li>
</ol>)

      

    

<p>Registers a font set under a font name.</p>
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
<ul>
<li><code>fallbackFontFilePaths</code> Additional font files are intended to be used if main font
does not contain required character symbol and shall be sorted starting from most useful.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void registerFontWithFallback(String fontName, String fontPath, List&lt;String&gt; fallbackFontFilePaths);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "MapMarkerTextStyle.withFont constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarkertextstyle-mapmarkertextstyle-withfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerTextStyle.withFont.html -->


<div>
<h1>MapMarkerTextStyle.withFont constructor</h1></div>

MapMarkerTextStyle.withFont(<ol class="parameter-list"> <li>double textSize, </li>
<li>Color textColor, </li>
<li>double textOutlineSize, </li>
<li>Color textOutlineColor, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-mapview-mapmarkertextstyleplacement">MapMarkerTextStylePlacement</a>&gt; placements, </li>
<li>String fontName, </li>
</ol>)
    

<p>Creates a set of styling options for the text of a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<p>List of placements is used to specify allowed placement of text relative to the icon.
When marker overlapping is allowed as set by <a href="sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed">MapMarker.isOverlapAllowed</a>,
only first placement element is considered.
Otherwise the placement value is chosen so that the text does not overlap
with other <code>MapMarker</code> instances.</p>
<p>Placement values are prioritized according
to the order in which they appear in the list. Lists with duplicate entries
as well as empty lists are not supported.</p>
<ul>
<li>
<p><code>textSize</code> The size of the text in pixels.
Only positive values are supported.</p>
</li>
<li>
<p><code>textColor</code> The text color.</p>
</li>
<li>
<p><code>textOutlineSize</code> The size of the text outline in pixels.
Only non-negative values are supported.</p>
</li>
<li>
<p><code>textOutlineColor</code> The color of the text outline.</p>
</li>
<li>
<p><code>placements</code> List of allowed placements of the text relative to the icon of a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>.</p>
</li>
<li>
<p><code>fontName</code> Font name, registered with <code>AssetsManager.registerFont</code>.
If empty string is provided, a default font will be used.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapmarkertextstyleinstantiationexception-class">MapMarkerTextStyleInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarkerTextStyle.withFont(double textSize, ui.Color textColor, double textOutlineSize, ui.Color textOutlineColor, List&lt;MapMarkerTextStylePlacement&gt; placements, String fontName) =&gt; $prototype.withFont(textSize, textColor, textOutlineSize, textOutlineColor, placements, fontName);</code></pre>

 



</div>
`
}</HTMLBlock>

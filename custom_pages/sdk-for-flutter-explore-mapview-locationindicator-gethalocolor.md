---
title: "getHaloColor abstract method"
slug: "sdk-for-flutter-explore-mapview-locationindicator-gethalocolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getHaloColor.html -->


<div>
<h1>getHaloColor abstract method</h1></div>

Color
getHaloColor(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a> style</li>
</ol>)

      

    

<p>Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.</p>
<p>The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.</p>
<ul>
<li><code>style</code> The type of IndicatorStyle for which the color should be returned.</li>
</ul>
<p>Returns <code>ui.Color</code>. The color of the halo for the specified IndicatorStyle.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ui.Color getHaloColor(LocationIndicatorIndicatorStyle style);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "CustomWarningProvider constructor"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-customwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarningProvider.html -->


<div>
<h1>CustomWarningProvider constructor</h1></div>

CustomWarningProvider(<ol class="parameter-list single-line"> <li>int getCustomWarningTypeLambda(), </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a>&gt; getWarningsLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>, </li>
<li><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>?</li>
</ol>)</li>
</ol>)
    

<p>A abstract class representing a provider of custom warnings based on vehicle position.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CustomWarningProvider(
  int Function() getCustomWarningTypeLambda,
  List&lt;CustomWarning&gt; Function(SegmentData, SegmentData?) getWarningsLambda,

) =&gt; CustomWarningProvider$Lambdas(
  getCustomWarningTypeLambda,
  getWarningsLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>

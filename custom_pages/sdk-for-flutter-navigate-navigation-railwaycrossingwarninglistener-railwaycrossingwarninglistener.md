---
title: "RailwayCrossingWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarningListener.html -->


<div>
<h1>RailwayCrossingWarningListener constructor</h1></div>

RailwayCrossingWarningListener(<ol class="parameter-list single-line"> <li>void onRailwayCrossingWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive railway crossing warnings.</p>
<p><strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
<code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RailwayCrossingWarningListener(
  void Function(RailwayCrossingWarning) onRailwayCrossingWarningUpdatedLambda,

) =&gt; RailwayCrossingWarningListener$Lambdas(
  onRailwayCrossingWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>

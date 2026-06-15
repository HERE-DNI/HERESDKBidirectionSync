---
title: "onTruckRestrictionsWarningUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-ontruckrestrictionswarningupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onTruckRestrictionsWarningUpdated.html -->


<div>
<h1>onTruckRestrictionsWarningUpdated abstract method</h1></div>

void
onTruckRestrictionsWarningUpdated(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a>&gt; restrictions</li>
</ol>)

      

    

<p>Called whenever the distance type (<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype">TruckRestrictionWarning.distanceType</a>) of a truck
restriction changes.</p>
<p>If needed, it is up to the application to maintain a list of active
warnings like the ones with <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> or <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> based on the
updates provided by this method.</p>
<ul>
<li><code>restrictions</code> A list containing truck restriction warnings that have their distance
type (<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype">TruckRestrictionWarning.distanceType</a>) updated.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onTruckRestrictionsWarningUpdated(List&lt;TruckRestrictionWarning&gt; restrictions);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "TrafficMergeWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarningListener-class.html -->


<div>
<h1>TrafficMergeWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive traffic merge warnings.</p>
<p><strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
which is given when the location of the traffic merge is reached.
A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener">TrafficMergeWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-ontrafficmergewarningupdated">onTrafficMergeWarningUpdated</a></li><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

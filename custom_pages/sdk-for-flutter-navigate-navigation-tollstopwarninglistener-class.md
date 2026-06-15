---
title: "TollStopWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStopWarningListener-class.html -->


<div>
<h1>TollStopWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive information on the upcoming toll booth structure.</p>
<p>The warner might also warn about gates/checkpoints for vignette, border checkpoints
and similar structures on the street.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
A <code>TollStop</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TollStop</code> 120 meters and <code>TollStop</code> 160 meters ahead,
the first <code>TollStop.distance_to_toll_stop_in_meters</code> is 120 meters
and the next <code>TollStop.distance_to_toll_stop_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tollstopwarninglistener">TollStopWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-ontollstopwarning">onTollStopWarning</a></li><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

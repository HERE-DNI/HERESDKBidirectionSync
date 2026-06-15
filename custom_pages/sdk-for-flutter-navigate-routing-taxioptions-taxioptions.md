---
title: "TaxiOptions constructor"
slug: "sdk-for-flutter-navigate-routing-taxioptions-taxioptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TaxiOptions.html -->


<div>
<h1>TaxiOptions constructor</h1></div>

TaxiOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a> routeOptions, </li>
<li><a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a> textOptions, </li>
<li><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> avoidanceOptions</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>routeOptions</code> Specifies the common route calculation options.</li>
<li><code>textOptions</code> Customize textual content returned from the route calculation, such
as localization, format, and unit system.</li>
<li><code>avoidanceOptions</code> Options to specify restrictions for route calculations. By default
no restrictions are applied.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaxiOptions(this.routeOptions, this.textOptions, this.avoidanceOptions)
    : tollOptions = TollOptions(), lastCharacterOfLicensePlate = null, maxSpeedOnSegments = [], allowDriveThroughTaxiRoads = true, carSpecifications = CarSpecifications();</code></pre>

 



</div>
`
}</HTMLBlock>

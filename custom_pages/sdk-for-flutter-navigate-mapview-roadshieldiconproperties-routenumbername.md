---
title: "routeNumberName property"
slug: "sdk-for-flutter-navigate-mapview-roadshieldiconproperties-routenumbername"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- routeNumberName.html -->


<div>
<h1>routeNumberName property</h1></div>

        
        String
        routeNumberName
<div class="features">getter/setter pair</div>


<p>A string that is used to additionally determine the road shield's visual representation.
In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
is available for each <code>Span</code> of a <code>Route</code> object.
Typically, the string contains the number of a road, such as "E100". Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
of a road shield icon.</p>
<p>Note that the actual text which will be displayed on the road shield icon is set with
<a href="/sdk-for-flutter-navigate-mapview-roadshieldiconproperties-shieldtext">RoadShieldIconProperties.shieldText</a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
shield. In this case an empty string should be passed.</p>
<p><strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
and without a cardinal direction.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String routeNumberName;</code></pre>

 



</div>
`
}</HTMLBlock>

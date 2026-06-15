---
title: "match abstract method"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-match"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- match.html -->


<div>
<h1>match abstract method</h1></div>

<a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>?
match(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-location-class">Location</a> location</li>
</ol>)

      

    

<p>This method computes the map-matched location for the provided input location.</p>
<p>Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found
within that radius, <code>null</code> is returned.</p>
<p>It's required to set <code>time</code> field for each <code>Location</code> object for the <code>MapMatcher</code> to work properly. In case no time is provided,
<code>null</code> is returned and an error message is logged. It is used to calculate the distance in time between
consecutive matches. Together with <code>speed</code>, this allows to calculate how likely a match is consistent with a previous match.
To improve matching accuracy, it is recommended to provide <code>bearing</code> and <code>speed</code> parameters for each <code>Location</code> object.</p>
<ul>
<li><code>location</code> The input location.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation?</a>. map-matched location or <code>null</code> if the location could not be matched to a road network.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMatchedLocation? match(Location location);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "customLocationIndicator property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customLocationIndicator.html -->


<div>
<h1>customLocationIndicator property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>?
customLocationIndicator


<p>Custom location indicator <a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> which <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses instead of the default.
If set, the user is responsible for adding and removing the object to/from the mapview.
It is important to stop sending location updates to the provided <a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, since
<a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and
stopRendering() calls. By default this property is <code>null</code>,
which means the default indicator is used, and <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> automatically adds and removes it to/from
the mapview upon startRendering() and stopRendering() calls.
Gets the currently set <code>LocationIndicator</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationIndicator? get customLocationIndicator;</code></pre>

</section>
<section id="setter">

void
customLocationIndicator=(<a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>? value)


<p>Custom location indicator <a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> which <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses instead of the default.
If set, the user is responsible for adding and removing the object to/from the mapview.
It is important to stop sending location updates to the provided <a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, since
<a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and
stopRendering() calls. By default this property is <code>null</code>,
which means the default indicator is used, and <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> automatically adds and removes it to/from
the mapview upon startRendering() and stopRendering() calls.
Sets a custom <a href="/sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, so that <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses the provided one instead
of the default.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set customLocationIndicator(LocationIndicator? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

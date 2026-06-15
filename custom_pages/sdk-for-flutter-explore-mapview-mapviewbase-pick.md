---
title: "pick abstract method"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-pick"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pick.html -->


<div>
<h1>pick abstract method</h1></div>

void
pick(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>? filter, </li>
<li><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a> viewArea, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a> callback</li>
</ol>)

      

    

<p>Returns all map content located inside the specified pick area.</p>
<p>Content to be picked is
specified by a pick content filter.
The pick area is defined by a rectangle in map view coordinates
in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner
of the map view.</p>
<ul>
<li>
<p><code>filter</code> Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
</li>
<li>
<p><code>viewArea</code> The rectangular pixel area of the view inside which map content will be picked.
View area is relative to the map view's origin at (0, 0) at the top-left corner
of the map view.</p>
</li>
<li>
<p><code>callback</code> Callback to call with the result. This will be called on a main thread when pick operation
completes.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void pick(MapSceneMapPickFilter? filter, Rectangle2D viewArea, MapViewBaseMapPickCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>

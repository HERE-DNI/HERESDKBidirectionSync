---
title: "TranslucentMapLayerGroup.withPriority constructor"
slug: "sdk-for-flutter-navigate-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TranslucentMapLayerGroup.withPriority.html -->


<div>
<h1>TranslucentMapLayerGroup.withPriority constructor</h1></div>

TranslucentMapLayerGroup.withPriority(<ol class="parameter-list single-line"> <li>String name, </li>
<li><a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a> aMap, </li>
<li><a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a> priority</li>
</ol>)
    

<p>Creates an instance of the group.</p>
<ul>
<li>
<p><code>name</code> Name of the group. Must be unique across <a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a> and <a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a>.</p>
</li>
<li>
<p><code>aMap</code> The map to attach the group to.</p>
</li>
<li>
<p><code>priority</code> The <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a> which should be applied to position the group.
The <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a> must contain only one priority and this priority must have no
category and no group, i.e. <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a> and
<a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a> should not be used when building the
<a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a>.
Example:</p>
</li>
</ul>
<p>new MapLayerPriorityBuilder().renderedAfterLayer("water").build()</p>
<p><code>MapLayerPriorityBuilder().renderedAfterLayer("water").build()</code></p>
<p>Throws <a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroupinstantiationexception-class">TranslucentMapLayerGroupInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TranslucentMapLayerGroup.withPriority(String name, HereMapControllerCore aMap, MapLayerPriority priority) =&gt; $prototype.withPriority(name, aMap, priority);</code></pre>

 



</div>
`
}</HTMLBlock>

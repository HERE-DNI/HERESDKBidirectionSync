---
title: "setPriority abstract method"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-setpriority"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPriority.html -->


<div>
<h1>setPriority abstract method</h1></div>

void
setPriority(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a> priority</li>
</ol>)

      

    

<p>Sets the render priority for the layer group which replaces any previously defined priority.</p>
<ul>
<li><code>priority</code> The priority to position the group.
The <a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a> must contain only one priority and this priority must have no
category and no group, i.e. <a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a> and
<a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a> should not be used when building the
<a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a>.
Example:</li>
</ul>
<p>new MapLayerPriorityBuilder().renderedAfterLayer("water").build()</p>
<p><code>MapLayerPriorityBuilder().renderedAfterLayer("water").build()</code></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setPriority(MapLayerPriority priority);</code></pre>

 



</div>
`
}</HTMLBlock>

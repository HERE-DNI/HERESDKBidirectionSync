---
title: "Maps / MapLayerPriorityBuilder"
slug: "sdk-for-ios-explore-api-reference-classes-maplayerprioritybuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerPriorityBuilder"></a>
<a title="MapLayerPriorityBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapLayerPriorityBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapLayerPriorityBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer
and its categories, relative to other layers or layer-category pairs.</p>
<p>Map layers are rendered in an order according to specified priorities. Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer’s default, main category is unnamed.</p>
<p>The concept of ‘category’ is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category ‘bridges’ and style
it accordingly in the style file. If the user does not intend to or cannot style elements
of the layer diffenrently then it should opt for a layer with only the default category (e.g.
raster layer).</p>
<p>One way to define layers’ priorities is by using a layer priority list in the scene configuration.</p>
<p>For example, a priority list in a scene configuration could define:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This means layer “background” is rendered first. Next up is layer “water”. Then category “outline” of
layer “roads”, followed by the main category of layer “roads”. Layer “labels” is then rendered last.</p>
<p><p>
Now let’s consider a newly created layer ‘zone’ and its categories:</p>
<ul>
<li>zone</li>
<li>zone:background</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
</ul>
<p>The user wants to alter the rendering order so that it looks like:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>road:outline</li>
<li>road</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its
<code>renderedBeforeLayer()</code> and <code>renderedAfterLayer()</code> member functions.</p>
<p>Note that the order of calls matters and one can use a previously defined layer or category
as a reference:</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">zoneLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span>     <span class="c1">// places "zone" after "water"</span>
                                              <span class="c1">// in the rendering order</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"background"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span>     <span class="c1">// places "zone:background" after "water"</span>
                                              <span class="c1">// in the rendering order and thus shifts</span>
                                              <span class="c1">// "zone" to be rendered later</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"lines-outline"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"road"</span><span class="p">)</span>      <span class="c1">// places "zone:lines-outline" after "road"</span>
                                              <span class="c1">// in the rendering order</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"lines"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"zone"</span><span class="p">,</span> <span class="nv">categoryName</span><span class="p">:</span> <span class="s">"lines-outline"</span><span class="p">)</span> <span class="c1">// places "zone:lines" after</span>
                                                                        <span class="c1">// "zone:lines-outline" in the rendering order</span>
      <span class="o">.</span><span class="nf">build</span><span class="p">();</span>

  <span class="n">zoneLayer</span><span class="o">.</span><span class="nf">setPriority</span><span class="p">(</span><span class="n">zoneLayerPriority</span><span class="p">);</span>  <span class="c1">// applies the priority to the zone layer</span>
                                            <span class="c1">// and its categories in one single operation.</span>
</code></pre>
<p>In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer
is going to be rendered last.</p>
<p>Due to a current limitation for point map layers, the mentioned APIs to control the rendering
order are not implemented. All labels will be rendered within the “labels” layer, defined in
the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is
allowed. The following categories can be used to have a different behaviour:</p>
<ul>
<li>‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of
the same category and block map labels.</li>
<li>‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed
to overlap with other labels of the same categoty and block map labels.</li>
<li>‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all
predefined categories, also map labels.
These categories are configured accordingly in the basic map
scene configurations.
Category assignment to features can be done in the style based on data attributes. The category
assignment can be done for all types of data: points, lines, polygons.</li>
</ul>
</p></section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of the layer priority builder interface.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withCategory(_:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">withCategory(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the layer category for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
After a priority is defined by calling one of the aforementioned functions, the current category
is cleared and the builder refers again to the layer itself.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withCategory</span><span class="p">(</span><span class="n">_</span> <span class="nv">category</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The name of the layer category.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/inGroup(_:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF">inGroup(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the group for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
When a group is set, the next defined priority is relative to the layers and layer categories
inside this group. The references (i.e. ‘referenceLayer’ and ‘referenceCategory’) of the priority
are only searched inside the group.
Only one group or no group can be defined per layer priority and layer category priority, however,
different layers can set priorities for the same group.
After a priority is defined by calling one of the aforementioned functions, the current group
is cleared and the builder refers again to the global layer list in the scene.
Note that a group needs to exist when the built <code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code> is used during a
<code><a href="../Classes/MapLayerBuilder.html#/s:7heresdk15MapLayerBuilderC5buildAA0bC0CyKF">MapLayerBuilder.build(...)</a></code> or <code><a href="../Classes/MapLayer.html#/s:7heresdk8MapLayerC11setPriorityyyAA0bcE0CF">MapLayer.setPriority(...)</a></code>, otherwise the priority
cannot be applied and the layer will render nothing to the group.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">inGroup</span><span class="p">(</span><span class="n">_</span> <span class="nv">group</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>group</em>
</code>
</td>
<td>
<div>
<p>The name of the group. For instance the name of a <code><a href="sdk-for-ios-explore-api-reference-..-classes-translucentmaplayergroup">TranslucentMapLayerGroup</a></code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC13renderedFirstACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedFirst()"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC13renderedFirstACyF">renderedFirst()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered before all layers and categories. Applies to the layer itself or the
category pointed to by the preceding call to <code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedFirst</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC12renderedLastACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedLast()"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC12renderedLastACyF">renderedLast()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered after all layers and categories. Applies to the layer itself or the
category pointed to by the preceding call to <code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedLast</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC014renderedBeforeC05namedACSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedBeforeLayer(named:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC014renderedBeforeC05namedACSS_tF">renderedBeforeLayer(named:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered before the first one from the referenceLayer and its categories.
Applies to the layer itself or the category pointed to by the preceding call to
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.
If the referenceLayer does not exist, then the function will set the priority as rendered
before all layers and categories.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedBeforeLayer</span><span class="p">(</span><span class="n">named</span> <span class="nv">referenceLayer</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>referenceLayer</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined layer name which renders directly after the current layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC014renderedBeforeC05named12categoryNameACSS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedBeforeLayer(named:categoryName:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC014renderedBeforeC05named12categoryNameACSS_SStF">renderedBeforeLayer(named:<wbr/>categoryName:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the
layer itself or the category pointed to by the preceding call to
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.
If the referenceLayer and/or the referenceCategory do not exist, then the function will set
the priority as rendered before all layers and categories.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedBeforeLayer</span><span class="p">(</span><span class="n">named</span> <span class="nv">referenceLayer</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="n">categoryName</span> <span class="nv">referenceCategory</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>referenceLayer</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined layer name which renders directly after the current layer.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>referenceCategory</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined category name which renders directly after the current layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC013renderedAfterC05namedACSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedAfterLayer(named:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC013renderedAfterC05namedACSS_tF">renderedAfterLayer(named:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered after the last one from the referenceLayer and its categories.
Applies to the layer itself or the category pointed to by the preceding call to
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.
If the referenceLayer does not exist, then the function will set the priority as rendered
after all layers and categories.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="n">named</span> <span class="nv">referenceLayer</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>referenceLayer</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined layer name which renders directly before the current layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC013renderedAfterC05named12categoryNameACSS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/renderedAfterLayer(named:categoryName:)"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC013renderedAfterC05named12categoryNameACSS_SStF">renderedAfterLayer(named:<wbr/>categoryName:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the
layer itself or the category pointed to by the preceding call to
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category ‘C’ after layer ‘L’ would be overridden by the priority to
render layer category ‘C’ before layer ‘L’ when building something like</p>
<p>withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)
<code>withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")</code>
The previously defined and prioritised categories can be used as reference.
If the referenceLayer and/or the referenceCategory do not exist, then the function will set
the priority as rendered after all layers and categories.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="n">named</span> <span class="nv">referenceLayer</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="n">categoryName</span> <span class="nv">referenceCategory</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>referenceLayer</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined layer name which renders directly before the current layer.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>referenceCategory</em>
</code>
</td>
<td>
<div>
<p>The beforehand defined category name which renders directly before the current layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC5buildAA0bcD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC5buildAA0bcD0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new
MapLayerPriority.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A new MapLayerPriority instance.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>

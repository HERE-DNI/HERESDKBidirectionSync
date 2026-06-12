---
title: "inGroup abstract method"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- inGroup.html -->


<div>
<h1>inGroup abstract method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>
inGroup(<ol class="parameter-list single-line"> <li>String group</li>
</ol>)

      

    

<p>Sets the group for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.</p>
<p>When a group is set, the next defined priority is relative to the layers and layer categories
inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority
are only searched inside the group.
Only one group or no group can be defined per layer priority and layer category priority, however,
different layers can set priorities for the same group.
After a priority is defined by calling one of the aforementioned functions, the current group
is cleared and the builder refers again to the global layer list in the scene.
Note that a group needs to exist when the built <a href="/sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a> is used during a
<a href="/sdk-for-flutter-explore-mapview-maplayerbuilder-build">MapLayerBuilder.build</a> or <a href="/sdk-for-flutter-explore-mapview-maplayer-setpriority">MapLayer.setPriority</a>, otherwise the priority
cannot be applied and the layer will render nothing to the group.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>group</code> The name of the group. For instance the name of a <a href="/sdk-for-flutter-explore-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a>.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder inGroup(String group);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "MapLayerPriorityBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapLayerPriorityBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapLayerPriorityBuilder</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapLayerPriorityBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer
 and its categories, relative to other layers or layer-category pairs.
 Map layers are rendered in an order according to specified priorities. Rendering order of elements in
 a single map layer can be controlled with categories. Layer names are unique, and category names have
 to be unique within a layer. The layer's default, main category is unnamed.
 The concept of 'category' is tightly linked to styling. The idea behind category is that
 one should be able to style separately elements in a map layer. Take, for instance, roads.
 If one wants to style separately the bridges it will create a category 'bridges' and style
 it accordingly in the style file. If the user does not intend to or cannot style elements
 of the layer diffenrently then it should opt for a layer with only the default category (e.g.
 raster layer).
 One way to define layers' priorities is by using a layer priority list in the scene configuration.
 For example, a priority list in a scene configuration could define:
 <ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
This means layer "background" is rendered first. Next up is layer "water". Then category "outline" of
 layer "roads", followed by the main category of layer "roads". Layer "labels" is then rendered last.
 
 Now let's consider a newly created layer 'zone' and its categories:
 <ul>
<li>zone</li>
<li>zone:background</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
</ul>
The user wants to alter the rendering order so that it looks like:
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
This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its
 <code>renderedBeforeLayer()</code> and <code>renderedAfterLayer()</code> member functions.
 Note that the order of calls matters and one can use a previously defined layer or category
 as a reference:
 <pre><code>MapLayerPriority zoneLayerPriority = new MapLayerPriorityBuilder()
       .renderedAfterLayer("water")            // places "zone" after "water"
                                               // in the rendering order
       .withCategory("background")
       .renderedAfterLayer("water")            // places "zone:background" after "water"
                                               // in the rendering order and thus shifts
                                               // "zone" to be rendered later
       .withCategory("lines-outline")
       .renderedAfterLayer("road")             // places "zone:lines-outline" after "road"
                                               // in the rendering order
       .withCategory("lines")
       .renderedAfterLayer("zone", "lines-outline") // places "zone:lines" after
                                               // "zone:lines-outline" in the rendering order
      .build();

  zoneLayer.setPriority(zoneLayerPriority);    // applies the priority to the zone layer
                                               // and its categories in one single operation.
  </code></pre>
In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer
 is going to be rendered last.
 Due to a current limitation for point map layers, the mentioned APIs to control the rendering
 order are not implemented. All labels will be rendered within the "labels" layer, defined in
 the scene configuration file.
 By default, all labels rendered by a point map layer are rendered last and no overlapping is
 allowed. The following categories can be used to have a different behaviour:
 <ul>
<li>'custom-labels' A label should be rendered first, is allowed to overlap with other labels of
 the same category and block map labels.</li>
<li>'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed
 to overlap with other labels of the same categoty and block map labels.</li>
<li>'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all
 predefined categories, also map labels.
 These categories are configured accordingly in the basic map
 scene configurations.
 Category assignment to features can be done in the style based on data attributes. The category
 assignment can be done for all types of data: points, lines, polygons.</li>
</ul></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#%3Cinit%3E()">MapLayerPriorityBuilder</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of the layer priority builder interface.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>MapLayerPriorityBuilder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapLayerPriorityBuilder</span>()</div>
<div className="block"><p>Creates an instance of the layer priority builder interface.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="withCategory(java.lang.String)">
<h3>withCategory</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">withCategory</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</span></div>
<div className="block"><p>Sets the layer category for which a priority could be defined with the next call to the functions
 <code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
 After a priority is defined by calling one of the aforementioned functions, the current category
 is cleared and the builder refers again to the layer itself.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The name of the layer category.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="inGroup(java.lang.String)">
<h3>inGroup</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">inGroup</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div className="block"><p>Sets the group for which a priority could be defined with the next call to the functions
 <code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
 When a group is set, the next defined priority is relative to the layers and layer categories
 inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority
 are only searched inside the group.
 Only one group or no group can be defined per layer priority and layer category priority, however,
 different layers can set priorities for the same group.
 After a priority is defined by calling one of the aforementioned functions, the current group
 is cleared and the builder refers again to the global layer list in the scene.
 Note that a group needs to exist when the built <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> is used during a
 <a href="sdk-for-android-navigate-maplayerbuilder#build()"><code>MapLayerBuilder.build()</code></a> or <a href="sdk-for-android-navigate-maplayer#setPriority(com.here.sdk.mapview.MapLayerPriority)"><code>MapLayer.setPriority(com.here.sdk.mapview.MapLayerPriority)</code></a>, otherwise the priority
 cannot be applied and the layer will render nothing to the group.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>group</code> - <p>The name of the group. For instance the name of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup</code></a>.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedFirst()">
<h3>renderedFirst</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedFirst</span>()</div>
<div className="block"><p>Sets the priority as rendered before all layers and categories. Applies to the layer itself or the
 category pointed to by the preceding call to <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedLast()">
<h3>renderedLast</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedLast</span>()</div>
<div className="block"><p>Sets the priority as rendered after all layers and categories. Applies to the layer itself or the
 category pointed to by the preceding call to <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedBeforeLayer(java.lang.String)">
<h3>renderedBeforeLayer</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedBeforeLayer</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceLayer)</span></div>
<div className="block"><p>Sets the priority as rendered before the first one from the referenceLayer and its categories.
 Applies to the layer itself or the category pointed to by the preceding call to
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.
 If the referenceLayer does not exist, then the function will set the priority as rendered
 before all layers and categories.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>referenceLayer</code> - <p>The beforehand defined layer name which renders directly after the current layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedBeforeLayer(java.lang.String,java.lang.String)">
<h3>renderedBeforeLayer</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedBeforeLayer</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceLayer,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceCategory)</span></div>
<div className="block"><p>Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the
 layer itself or the category pointed to by the preceding call to
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.
 If the referenceLayer and/or the referenceCategory do not exist, then the function will set
 the priority as rendered before all layers and categories.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>referenceLayer</code> - <p>The beforehand defined layer name which renders directly after the current layer.</p></dd>
<dd><code>referenceCategory</code> - <p>The beforehand defined category name which renders directly after the current layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedAfterLayer(java.lang.String)">
<h3>renderedAfterLayer</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedAfterLayer</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceLayer)</span></div>
<div className="block"><p>Sets the priority as rendered after the last one from the referenceLayer and its categories.
 Applies to the layer itself or the category pointed to by the preceding call to
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.
 If the referenceLayer does not exist, then the function will set the priority as rendered
 after all layers and categories.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>referenceLayer</code> - <p>The beforehand defined layer name which renders directly before the current layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="renderedAfterLayer(java.lang.String,java.lang.String)">
<h3>renderedAfterLayer</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span className="element-name">renderedAfterLayer</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceLayer,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceCategory)</span></div>
<div className="block"><p>Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the
 layer itself or the category pointed to by the preceding call to
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String)"><code>withCategory(java.lang.String)</code></a>.
 Notice that the order of calls to the functions
 <code>renderedFirst|Last|Before|After</code>
 matters, and that after such a call the builder clears the current category and refers again to
 the layer itself. Further, only one priority for each layer and layer category should be set
 with these functions since previous priorities would be ingored. For example the priority to
 render layer category 'C' after layer 'L' would be overridden by the priority to
 render layer category 'C' before layer 'L' when building something like
 <code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code>
The previously defined and prioritised categories can be used as reference.
 If the referenceLayer and/or the referenceCategory do not exist, then the function will set
 the priority as rendered after all layers and categories.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>referenceLayer</code> - <p>The beforehand defined layer name which renders directly before the current layer.</p></dd>
<dd><code>referenceCategory</code> - <p>The beforehand defined category name which renders directly before the current layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="build()">
<h3>build</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a></span> <span className="element-name">build</span>()</div>
<div className="block"><p>Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new
 MapLayerPriority.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A new MapLayerPriority instance.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>

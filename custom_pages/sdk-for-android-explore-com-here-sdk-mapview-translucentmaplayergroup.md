---
title: "TranslucentMapLayerGroup (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TranslucentMapLayerGroup.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.TranslucentMapLayerGroup</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TranslucentMapLayerGroup</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A translucent layer group that can be the target for <a href="sdk-for-android-explore-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a>.
 Currently, only custom line layers can be added to a translucent layer group.
 Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so
 that overlapping translucent line geometry is not alpha blended with itself.
 At creation, the layer group gets added to a map. The layer group gets removed from the map upon
 instance destruction and any layer (categories) still in the group are not rendered anymore,
 therefore it is recommended to keep a group alive as long as layers using the group are alive and
 in use.
 Conceptual example to place line layers into a translucent group:
 <pre><code>// Create a translucent group with a unique name and a render priority
  MapLayerPriority groupPriority = new MapLayerPriorityBuilder().renderedLast().build();
  TranslucentMapLayerGroup group = new TranslucentMapLayerGroup("TranslucentGroupName", map, groupPriority)

  // Create a line layer to be rendered as part of the translucent group
  MapLayerPriority lineLayerPriority = new MapLayerPriorityBuilder()
      .inGroup("TranslucentGroupName") // places the line layer into the group
      .renderedFirst()                 // to be rendered first when the group is rendered
      .withCategory("SomeCategory")    // places the line layer category 'SomeCategory'
      .inGroup("TranslucentGroupName") // into the group
      .renderedLast()                  // to be rendered last when the group is rendered
      .build();

  MapLayer lineLayer = new MapLayerBuilder()
      .withDataSource("DataSourceName", MapContentType.LINE)
      .forMap(map)
      .withName("LineLayerName")
      .withPriority(lineLayerPriority)
      .withStyle(translucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
      .build();

  // Create a second line layer to be rendered as part of the translucent group
  MapLayerPriority secondLineLayerPriority = new MapLayerPriorityBuilder()
      .inGroup("TranslucentGroupName")      // places the second line layer into the group
      .renderedBeforeLayer("LineLayerName") // to be rendered before first layer
                                            // when the group is rendered
      .build();

  MapLayer secondLineLayer = new MapLayerBuilder()
      .withDataSource("SecondDataSourceName", MapContentType.LINE)
      .forMap(map)
      .withName("SecondLineLayerName")
      .withPriority(secondLineLayerPriority)
      .withStyle(secondTranslucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
      .build();
  </code></pre>
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errorcode" title="enum class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Error codes for creating the group.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errordetails" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorDetails</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Describes the reason for failing to create the group.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code></div>
<div class="col-last even-row-color">
<div class="block">Thrown when failing to build the group.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap)">TranslucentMapLayerGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the group.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)">TranslucentMapLayerGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of the group.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frees all internally used resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup#setPriority(com.here.sdk.mapview.MapLayerPriority)">setPriority</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the render priority for the layer group which replaces any previously defined priority.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.HereMap)">
<h3>TranslucentMapLayerGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TranslucentMapLayerGroup</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap)</span>
                         throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></span></div>
<div class="block"><p>Creates an instance of the group.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Name of the group. Must be unique across <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a> and <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup</code></a>.</p></dd>
<dd><code>aMap</code> - <p>The map to attach the group to.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)">
<h3>TranslucentMapLayerGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TranslucentMapLayerGroup</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</span>
                         throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></span></div>
<div class="block"><p>Creates an instance of the group.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Name of the group. Must be unique across <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a> and <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup</code></a>.</p></dd>
<dd><code>aMap</code> - <p>The map to attach the group to.</p></dd>
<dd><code>priority</code> - <p>The <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> which should be applied to position the group.
     The <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no
     category and no group, i.e. <a href="sdk-for-android-explore-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a> and
     <a href="sdk-for-android-explore-maplayerprioritybuilder#withCategory(java.lang.String)"><code>MapLayerPriorityBuilder.withCategory(java.lang.String)</code></a> should not be used when building the
     <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a>.
     Example:
     <code>new MapLayerPriorityBuilder().renderedAfterLayer(&amp;quot;water&amp;quot;).build()</code></p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="setPriority(com.here.sdk.mapview.MapLayerPriority)">
<h3>setPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPriority</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</span></div>
<div class="block"><p>Sets the render priority for the layer group which replaces any previously defined priority.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>priority</code> - <p>The priority to position the group.
     The <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no
     category and no group, i.e. <a href="sdk-for-android-explore-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a> and
     <a href="sdk-for-android-explore-maplayerprioritybuilder#withCategory(java.lang.String)"><code>MapLayerPriorityBuilder.withCategory(java.lang.String)</code></a> should not be used when building the
     <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a>.
     Example:
     <code>new MapLayerPriorityBuilder().renderedAfterLayer(&amp;quot;water&amp;quot;).build()</code></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block"><p>Frees all internally used resources. After calling this method, the object is not usable
 anymore.</p></div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>

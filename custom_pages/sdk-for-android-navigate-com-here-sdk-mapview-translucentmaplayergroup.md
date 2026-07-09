---
title: "TranslucentMapLayerGroup (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TranslucentMapLayerGroup.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.TranslucentMapLayerGroup</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TranslucentMapLayerGroup</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A translucent layer group that can be the target for <a href="sdk-for-android-navigate-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a>.
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
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-errorcode" title="enum class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Error codes for creating the group.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-errordetails" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorDetails</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Describes the reason for failing to create the group.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code></div>
<div className="col-last even-row-color">
<div className="block">Thrown when failing to build the group.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap)">TranslucentMapLayerGroup</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of the group.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)">TranslucentMapLayerGroup</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates an instance of the group.</div>
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
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.HereMap)">
<h3>TranslucentMapLayerGroup</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TranslucentMapLayerGroup</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap)</span>
                         throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></span></div>
<div className="block"><p>Creates an instance of the group.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Name of the group. Must be unique across <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup</code></a>.</p></dd>
<dd><code>aMap</code> - <p>The map to attach the group to.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)">
<h3>TranslucentMapLayerGroup</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TranslucentMapLayerGroup</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a> aMap,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</span>
                         throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></span></div>
<div className="block"><p>Creates an instance of the group.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Name of the group. Must be unique across <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup</code></a>.</p></dd>
<dd><code>aMap</code> - <p>The map to attach the group to.</p></dd>
<dd><code>priority</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> which should be applied to position the group.
     The <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no
     category and no group, i.e. <a href="sdk-for-android-navigate-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a> and
     <a href="sdk-for-android-navigate-maplayerprioritybuilder#withCategory(java.lang.String)"><code>MapLayerPriorityBuilder.withCategory(java.lang.String)</code></a> should not be used when building the
     <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a>.
     Example:
     <code>new MapLayerPriorityBuilder().renderedAfterLayer("water").build()</code></p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
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
<section className="detail" id="setPriority(com.here.sdk.mapview.MapLayerPriority)">
<h3>setPriority</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPriority</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</span></div>
<div className="block"><p>Sets the render priority for the layer group which replaces any previously defined priority.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>priority</code> - <p>The priority to position the group.
     The <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no
     category and no group, i.e. <a href="sdk-for-android-navigate-maplayerprioritybuilder#inGroup(java.lang.String)"><code>MapLayerPriorityBuilder.inGroup(java.lang.String)</code></a> and
     <a href="sdk-for-android-navigate-maplayerprioritybuilder#withCategory(java.lang.String)"><code>MapLayerPriorityBuilder.withCategory(java.lang.String)</code></a> should not be used when building the
     <a href="sdk-for-android-navigate-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview"><code>MapLayerPriority</code></a>.
     Example:
     <code>new MapLayerPriorityBuilder().renderedAfterLayer("water").build()</code></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroy()">
<h3>destroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroy</span>()</div>
<div className="block"><p>Frees all internally used resources. After calling this method, the object is not usable
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
</div>



</div>
`
}</HTMLBlock>

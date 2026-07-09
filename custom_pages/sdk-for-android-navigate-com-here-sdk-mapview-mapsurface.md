---
title: "MapSurface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapsurface"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSurface.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapSurface</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">MapSurface</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></span></div>
<div className="block">Provides the ability to render a map into a provided rendering surface. This enables the
 possibility to render a map into external displays like Android Auto. If you want to use the
 map for a regular use case please use the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview"><code>MapView</code></a> instead.</div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface-renderlistener" title="interface in com.here.sdk.mapview">MapSurface.RenderListener</a></code></div>
<div className="col-last even-row-color">
<div className="block">Listener of MapSurface render events.</div>
</div>
</div>
<div className="inherited-list">

<code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase-mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#%3Cinit%3E()">MapSurface</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#%3Cinit%3E(android.content.Context)">MapSurface</a><wbr/>(android.content.Context context)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#%3Cinit%3E(android.content.Context,com.here.sdk.mapview.MapViewOptions)">MapSurface</a><wbr/>(android.content.Context context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#%3Cinit%3E(com.here.sdk.mapview.MapViewOptions)">MapSurface</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
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
<h3>MapSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapSurface</span>()</div>
<div className="block">Creates a new instance.</div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapViewOptions)">
<h3>MapSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapSurface</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - The options</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context)">
<h3>MapSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapSurface</span><wbr/><span className="parameters">(android.content.Context context)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Application context</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context,com.here.sdk.mapview.MapViewOptions)">
<h3>MapSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapSurface</span><wbr/><span className="parameters">(android.content.Context context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - The options</dd>
<dd><code>context</code> - The Application context</dd>
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
<section className="detail" id="isValid()">
<h3>isValid</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isValid</span>()</div>
<div className="block">Returns whether this <code>MapSurface</code> is valid. An invalid <code>MapSurface</code> is
 non-functional. A <code>MapSurface</code> is considered valid only after <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#attachSurface(android.content.Context,android.view.Surface,int,int)"><code>attachSurface(Context, Surface, int, int)</code></a> and before <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#destroy()"><code>destroy()</code></a> is called.
 <code>MapSurface</code> is also invalidated when the
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> it is using is destroyed.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#isValid()">isValid</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if this <code>MapSurface</code> is valid, <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroy()">
<h3>destroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroy</span>()</div>
<div className="block">Destroys the map renderer and render surface, making this <code>MapSurface</code> invalid.
 Call this method only when the render surface will no longer be used.
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#isValid()"><code>isValid()</code></a> will return <code>false</code> after this is called.
 It can be made valid again by setting render surface using
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#attachSurface(android.content.Context,android.view.Surface,int,int)"><code>attachSurface(Context, Surface, int, int)</code></a>.</div>
</section>
</li>
<li>
<section className="detail" id="setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener)">
<h3>setOnReadyListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOnReadyListener</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview">MapView.OnReadyListener</a> readyListener)</span></div>
<div className="block">Sets the OnReadyListener, which will be notified once MapView initialization has
 been finished. It is highly recommended to put code that accesses map view related
 functionality inside <a href="sdk-for-android-navigate-mapview-onreadylistener#onMapViewReady()"><code>MapView.OnReadyListener.onMapViewReady()</code></a> instead of directly in
 <code>Activity</code>'s <code>onResume()</code>.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>readyListener</code> - The listener to be registered, or <code>null</code> to unregister any
                      previously register listener.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="attachSurface(android.content.Context,android.view.Surface,int,int)">
<h3>attachSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">attachSurface</span><wbr/><span className="parameters">(android.content.Context context,
 android.view.Surface surface,
 int width,
 int height)</span></div>
<div className="block">Sets the surface on which the map will be rendered. Throws exception if the surface
 cannot be used by HERESDK.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Application context</dd>
<dd><code>surface</code> - The surface to render to.</dd>
<dd><code>width</code> - The width of the render surface in pixels.</dd>
<dd><code>height</code> - The height of the render surface in pixels.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if surface is invalid and cannot be used.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="attachSurface(android.content.Context,android.view.Surface,int,int,com.here.sdk.mapview.MapSurface.RenderListener)">
<h3>attachSurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">attachSurface</span><wbr/><span className="parameters">(android.content.Context context,
 android.view.Surface surface,
 int width,
 int height,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface-renderlistener" title="interface in com.here.sdk.mapview">MapSurface.RenderListener</a> renderListener)</span></div>
<div className="block">Sets the surface on which the map will be rendered. Throws exception if the surface
 cannot be used by HERESDK.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Application context</dd>
<dd><code>surface</code> - The surface to render to.</dd>
<dd><code>width</code> - The width of the render surface in pixels.</dd>
<dd><code>height</code> - The height of the render surface in pixels.</dd>
<dd><code>renderListener</code> - A listener for render events. The listener will be released
                      once <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsurface#destroySurface()"><code>destroySurface()</code></a> gets called.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if surface is invalid and cannot be used.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroySurface()">
<h3>destroySurface</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroySurface</span>()</div>
<div className="block">Destroys the rendering surface.</div>
</section>
</li>
<li>
<section className="detail" id="redraw(java.lang.Runnable)">
<h3>redraw</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">redraw</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> redrawFinished)</span></div>
<div className="block"><p>Redraws the map and reports back on completion.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>redrawFinished</code> - <p>The runnable to be executed after completion.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">
<h3>pick</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">pick</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase-mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a> callback)</span></div>
<div className="block"><p>Returns all map content located inside the specified pick area. Content to be picked is
 specified by a pick content filter.
 The pick area is defined by a rectangle in map view coordinates
 in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner
 of the map view.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">pick</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>filter</code> - <p>Filter for the map content to be picked. When a filter is not set all of the
              pickable content will be picked.</p></dd>
<dd><code>viewArea</code> - <p>The rectangular pixel area of the view inside which map content will be
         picked.
     View area is relative to the map view's origin at (0, 0) at the top-left corner
     of the map view.</p></dd>
<dd><code>callback</code> - <p>Callback to call with the result. This will be called on a main thread
         when pick operation
     completes.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>geoToViewCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span className="element-name">geoToViewCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div className="block">Converts geographical coordinates to view coordinates (in pixels).
 <p>
 If specified, altitude of the input coordinates is interpreted as altitude above sea level.
 If not specified, the input coordinates are interpreted as being on ground elevation.
 The above distinction is only relevant when 3D terrain feature is enabled.
 
 The resulting view coordinates might be outside of current viewport, i.e. result might
 contain values less than zero or greater than view's dimensions.  If the render surface is
 not attached, it will return <code>null</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">geoToViewCoordinates</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>Geographical coordinates to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The view coordinates of the specified geographical point or <code>null</code>
     if there is no render surface attached.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>addLifecycleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addLifecycleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div className="block"><p>Adds a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to this map view.
 Adding the same object multiple times has no effect.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">addLifecycleListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - <p>An object to be notified of lifecycle events.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>removeLifecycleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeLifecycleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div className="block"><p>Removes a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from this map view.
 Trying to remove an object that was not added or was removed before
 has no effect.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">removeLifecycleListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - <p>An object to stop being notified of lifecycle events.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onResume()">
<h3>onResume</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onResume</span>()</div>
<div className="block"><p>Call this method in the onResume() method of the lifecycle owner.</p></div>
</section>
</li>
<li>
<section className="detail" id="onPause()">
<h3>onPause</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onPause</span>()</div>
<div className="block"><p>Call this method in the onPause() method of the lifecycle owner.</p></div>
</section>
</li>
<li>
<section className="detail" id="viewToGeoCoordinates(com.here.sdk.core.Point2D)">
<h3>viewToGeoCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">viewToGeoCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates)</span></div>
<div className="block">Converts view coordinates to geographical coordinates.
 <p>
 An optional altitude component of the resulting geographical coordinate is not set.
 
 If the view coordinates specify a point above a horizon, then the result
 is geographical coordinates of the point on a horizon below the specified
 view coordinates.
 
 The fog effect is ignored for the calculation, meaning that for the view point
 within the area covered by the fog, the result is geographical coordinates
 that would be displayed at the specified point if the fog effect was
 not applied.
 
 If the render surface is not attached, it will return <code>null</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#viewToGeoCoordinates(com.here.sdk.core.Point2D)">viewToGeoCoordinates</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>Point inside the view to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The geographical coordinates under specified view point or <code>null</code>
         if there is no render surface attached.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGestures()">
<h3>getGestures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures">Gestures</a></span> <span className="element-name">getGestures</span>()</div>
<div className="block">Returns the gestures control object. Please note that there is no gesture support for the
 MapSurface at this point.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getGestures()">getGestures</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> control object</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPixelScale()">
<h3>getPixelScale</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getPixelScale</span>()</div>
<div className="block"><p>Gets the pixel scale factor used by this MapView.
 It is used to support screen resolution and size independence.
 This value is a derivative of the device's screen pixel density
 and is a direct analog of pixel density from DisplayMetrics.
 It can be used to translate between physical pixels and
 density independent pixels according to formula:</p>
<p>dp = px / pixel_scale.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getPixelScale()">getPixelScale</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>current pixel scale factor, or 0.0 if MapView is not initialized</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getViewportSize()">
<h3>getViewportSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span className="element-name">getViewportSize</span>()</div>
<div className="block">Returns the viewport size of this MapView in physical pixels.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getViewportSize()">getViewportSize</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>The viewport size in physical pixels</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFrameRate()">
<h3>getFrameRate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getFrameRate</span>()</div>
<div className="block">Gets maximum render frame rate in frames per second. The default value is 60 frames per
 second.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getFrameRate()">getFrameRate</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>Actual maximal render frame rate</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setFrameRate(int)">
<h3>setFrameRate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setFrameRate</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block">Sets maximum render frame rate in frames per second.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#setFrameRate(int)">setFrameRate</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - Maximum render frame rate in frames per second. Setting to 0 disables automatic
 rendering for this view. Setting negative values has no effect.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="takeScreenshot(com.here.sdk.mapview.MapView.TakeScreenshotCallback)">
<h3>takeScreenshot</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">takeScreenshot</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-takescreenshotcallback" title="interface in com.here.sdk.mapview">MapView.TakeScreenshotCallback</a> callback)</span></div>
<div className="block">Asynchronously retrieves screenshot of current map view</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - Completion handler called when the screenshot is completed</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">
<h3>setWatermarkLocation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setWatermarkLocation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> offset)</span></div>
<div className="block"><p>Sets the position of the HERE logo watermark within the map view.

 By default, the watermark is aligned to the bottom-right corner of the view:
 Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
 It is recommended to change the default position only if necessary to avoid overlapping UI
 elements. The watermark should always be fully visible within the view. The anchor point on
 the watermark is its center (width/2, height/2), around which it will be placed in the map
 view. For map views smaller than 250 dip in both width and height, the watermark will not be
 shown.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">setWatermarkLocation</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>anchor</code> - <p>Anchor point in normalized view coordinates [0, 1]. Map view's origin at
     (0, 0) indicates a top-left corner of the map view.
     Out of boundary anchor point values will be clamped to the [0, 1] range.</p></dd>
<dd><code>offset</code> - <p>A horizontal and vertical offset (expressed in positive/negative pixel
     coordinates) that allows shifting the watermark from the anchor point position in one or
     the other direction.
     For the quadrant of values expressing visible part of the map view negative offset shifts
     the watermark to the direction of the origin, positive - away from it.
     For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
     the bottom.
     If specified offset will result in watermark being completely or partially out-of-view
     the offset will be adjusted internally so that watermark is fully visible.
     Offset is not being scaled when the map view size changes.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWatermarkSize()">
<h3>getWatermarkSize</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span className="element-name">getWatermarkSize</span>()</div>
<div className="block"><p>Returns the watermark size in physical pixels.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getWatermarkSize()">getWatermarkSize</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>Provides the size of the watermark in physical pixels.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setShadowQuality(com.here.sdk.mapview.ShadowQuality)">
<h3>setShadowQuality</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setShadowQuality</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-shadowquality" title="enum class in com.here.sdk.mapview">ShadowQuality</a> shadowQuality)</span></div>
<div className="block">Set desired shadow quality for all instances of MapSurface/MapView.
 The quality controls the size of the shadow maps and the cascade count.
 The default shadow quality is <code>ShadowQuality.MEDIUM</code>.
 MapSurfaces can request to render shadows by feature.
 Enabling shadows has a performance impact and should be considered only for devices with
 sufficient performance.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>shadowQuality</code> - The shadow quality.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getShadowQuality()">
<h3>getShadowQuality</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-shadowquality" title="enum class in com.here.sdk.mapview">ShadowQuality</a></span> <span className="element-name">getShadowQuality</span>()</div>
<div className="block">Gets the currently set shadow quality.
 The default shadow quality is <code>ShadowQuality.MEDIUM</code>.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The currently set shadow quality.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCamera()">
<h3>getCamera</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></span> <span className="element-name">getCamera</span>()</div>
<div className="block">Returns the camera control object for the map</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getCamera()">getCamera</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview"><code>MapCamera</code></a> object for the map</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMapScene()">
<h3>getMapScene</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview">MapScene</a></span> <span className="element-name">getMapScene</span>()</div>
<div className="block">Gets the map scene associated with this map view.
 This can be used to request different map schemes to be displayed in the map view, and to
 add and remove map items from the map.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getMapScene()">getMapScene</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMapContext()">
<h3>getMapContext</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a></span> <span className="element-name">getMapContext</span>()</div>
<div className="block">Gets the map context associated with this map view.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getMapContext()">getMapContext</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getHereMap()">
<h3>getHereMap</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a></span> <span className="element-name">getHereMap</span>()</div>
<div className="block">Gets the HereMap associated with this map view.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getHereMap()">getHereMap</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if MapSurface object is not valid.</dd>
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

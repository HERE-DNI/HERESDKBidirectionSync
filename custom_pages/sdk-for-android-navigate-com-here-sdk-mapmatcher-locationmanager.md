---
title: "LocationManager (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationManager.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapmatcher.LocationManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LocationManager</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div class="block"><p>LocationManager listens to position updates and provides the
 map-matched location using the LocationManagerListener.
 </p><p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
 behaviors. Related APIs may change in future releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">LocationManager</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#addMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">addMatchedLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> to the subscribtion list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called each time a new location is available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#removeMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">removeMatchedLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> from the subscribtion list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#setMapMatcher(com.here.sdk.mapmatcher.MapMatcher)">setMapMatcher</a><wbr/>(<a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a> mapMatcher)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> for exclusive use by <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#takeMapMatcher()">takeMapMatcher</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves and removes the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> from <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>LocationManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationManager</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
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
<section class="detail" id="setMapMatcher(com.here.sdk.mapmatcher.MapMatcher)">
<h3>setMapMatcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMapMatcher</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a> mapMatcher)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> for exclusive use by <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 </p><p><strong>Threading:</strong> This method is asynchronous and performs the switch in an internal thread of <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 <strong>Note:</strong> After calling this method, the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> is owned and used exclusively
 by <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a> in its internal processing thread.
 Do not use or access the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> elsewhere while it is set.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapMatcher</code> - <p>The <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> instance to be used exclusively by <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="takeMapMatcher()">
<h3>takeMapMatcher</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a></span> <span class="element-name">takeMapMatcher</span>()</div>
<div class="block"><p>Retrieves and removes the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> from <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 <strong>Note:</strong> After calling this method, <a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a> will no longer use the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> at all.
 the caller regains full ownership and responsibility for the <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> instance previously set, or <code>null</code> if none was set.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">
<h3>addMatchedLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMatchedLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span></div>
<div class="block"><p>Adds the <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> to the subscribtion list.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matchedLocationListener</code> - <p>Listener to be added to the map matched location updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">
<h3>removeMatchedLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMatchedLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span></div>
<div class="block"><p>Removes the <a href="sdk-for-android-navigate-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> from the subscribtion list.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matchedLocationListener</code> - <p>Listener to be removed from the map matched location updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>location</code> - <p>Current location.</p></dd>
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
`
}</HTMLBlock>

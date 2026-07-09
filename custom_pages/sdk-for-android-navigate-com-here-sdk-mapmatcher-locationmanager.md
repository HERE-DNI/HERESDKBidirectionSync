---
title: "LocationManager (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationManager.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapmatcher</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapmatcher.LocationManager</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LocationManager</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div className="block"><p>LocationManager listens to position updates and provides the
 map-matched location using the LocationManagerListener.
 <strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
 behaviors. Related APIs may change in future releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">LocationManager</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>LocationManager</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationManager</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
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
<section className="detail" id="setMapMatcher(com.here.sdk.mapmatcher.MapMatcher)">
<h3>setMapMatcher</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMapMatcher</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a> mapMatcher)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> for exclusive use by <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 <strong>Threading:</strong> This method is asynchronous and performs the switch in an internal thread of <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 <strong>Note:</strong> After calling this method, the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> is owned and used exclusively
 by <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a> in its internal processing thread.
 Do not use or access the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> elsewhere while it is set.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapMatcher</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> instance to be used exclusively by <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="takeMapMatcher()">
<h3>takeMapMatcher</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a></span> <span className="element-name">takeMapMatcher</span>()</div>
<div className="block"><p>Retrieves and removes the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> from <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a>.
 <strong>Note:</strong> After calling this method, <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher"><code>LocationManager</code></a> will no longer use the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> at all.
 the caller regains full ownership and responsibility for the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher"><code>MapMatcher</code></a> instance previously set, or <code>null</code> if none was set.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">
<h3>addMatchedLocationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMatchedLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span></div>
<div className="block"><p>Adds the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> to the subscribtion list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>matchedLocationListener</code> - <p>Listener to be added to the map matched location updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMatchedLocationListener(com.here.sdk.mapmatcher.MatchedLocationListener)">
<h3>removeMatchedLocationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMatchedLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span></div>
<div className="block"><p>Removes the <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher"><code>MatchedLocationListener</code></a> from the subscribtion list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>matchedLocationListener</code> - <p>Listener to be removed from the map matched location updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onLocationUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
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
</div>



</div>
`
}</HTMLBlock>

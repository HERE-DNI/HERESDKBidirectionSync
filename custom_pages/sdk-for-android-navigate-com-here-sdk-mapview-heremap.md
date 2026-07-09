---
title: "HereMap (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-heremap"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- HereMap.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.HereMap</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">HereMap</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>The representation of a dynamic and interactive geographic map.
 The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area.
 The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="addMapIdleListener(com.here.sdk.mapview.MapIdleListener)">
<h3>addMapIdleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapIdleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapidlelistener" title="interface in com.here.sdk.mapview">MapIdleListener</a> listener)</span></div>
<div className="block"><p>Adds a listener for receiving idle state
 notifications and notifies it of the current state.
 The first notification received is always the state at the time of registration.
 The new listener is appended to the set
 of <code>HereMap</code> idle listeners as a strong reference.
 The caller is responsible for releasing the strong reference by calling
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap#removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)"><code>removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)">
<h3>removeMapIdleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapIdleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapidlelistener" title="interface in com.here.sdk.mapview">MapIdleListener</a> listener)</span></div>
<div className="block"><p>Removes a listener from receiving idle state notifications.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStyle()">
<h3>getStyle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview">Style</a></span> <span className="element-name">getStyle</span>()</div>
<div className="block"><p>Gets the style that the map uses to customize the visual appearance of rendered features.
 Changes made to the map style using <a href="sdk-for-android-navigate-style#update(com.here.sdk.mapview.Style)"><code>Style.update(com.here.sdk.mapview.Style)</code></a> are lost when new scene is loaded using
 <a href="sdk-for-android-navigate-mapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a> and its variants as well as
 when map features are enabled or disabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a> and <a href="sdk-for-android-navigate-mapscene#disableFeatures(java.util.List)"><code>MapScene.disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The style that the map uses to customize the visual appearance of rendered features.</p></dd>
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

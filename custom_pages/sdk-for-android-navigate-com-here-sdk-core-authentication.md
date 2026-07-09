---
title: "Authentication (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-authentication"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Authentication.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.Authentication</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Authentication</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use the authentication class to authenticate and retrieve a secure token that
 can be used with other HERE services.</p></div>
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
<section className="detail" id="authenticate(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.core.AuthenticationCallback)">
<h3>authenticate</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">authenticate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</span></div>
<div className="block"><p>Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token. This method operates asynchronously.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkNativeEngine</code> - <p>The SDK engine instance.</p></dd>
<dd><code>callback</code> - <p>Callback to retrieve an authentication token on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="authenticate(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>authenticate</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-authenticationdata" title="class in com.here.sdk.core">AuthenticationData</a></span> <span className="element-name">authenticate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkNativeEngine)</span>
                                       throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-authenticationexception" title="class in com.here.sdk.core">AuthenticationException</a></span></div>
<div className="block"><p>Uses the authentication service that is connected to the given SDK engine to authenticate and
 retrieve a secure token. This method operates synchronously.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkNativeEngine</code> - <p>The SDK engine instance.</p></dd>
<dt>Returns:</dt>
<dd><p>Authentication data.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-authenticationexception" title="class in com.here.sdk.core">AuthenticationException</a></code> - <p>Authentication exception that describes the error.</p></dd>
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

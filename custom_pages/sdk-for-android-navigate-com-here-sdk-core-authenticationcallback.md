---
title: "AuthenticationCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-authenticationcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AuthenticationCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">AuthenticationCallback</span></div>
<div className="block"><p>Callback passed to <a href="sdk-for-android-navigate-authentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)"><code>Authentication.authenticate(SDKNativeEngine)</code></a>.
 This callback is called on the main thread asynchronously when an
 authenticate call has completed.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="onTokenReceived(com.here.sdk.core.AuthenticationError,com.here.sdk.core.AuthenticationData)">
<h3>onTokenReceived</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTokenReceived</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationerror" title="enum class in com.here.sdk.core">AuthenticationError</a> authenticationError,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationdata" title="class in com.here.sdk.core">AuthenticationData</a> authenticationData)</span></div>
<div className="block"><p>Callback passed to <a href="sdk-for-android-navigate-authentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)"><code>Authentication.authenticate(SDKNativeEngine)</code></a>.
 This callback is called on the main thread asynchronously when an
 authenticate call has completed.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>authenticationError</code> - <p>Represents the operation status. It is 'null' for an operation that succeeds.</p></dd>
<dd><code>authenticationData</code> - <p>Represents the authentication data.</p></dd>
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

---
title: "AuthenticationMode (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AuthenticationMode.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.AuthenticationMode</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AuthenticationMode</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This is a bearer authentication mode which adds or does not add a
 header ("Authorization", "Bearer $Token") to each online request of the
 module the object is added to. The token (if used) can be provided or is
 retrieved via key/secret from a dedicated backend.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode-accesstokenprovider" title="interface in com.here.sdk.core.engine">AuthenticationMode.AccessTokenProvider</a></code></div>
<div className="col-last even-row-color">
<div className="block">This lambda is used to retrieve access token in synchronous manner.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> rhs)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withToken(java.lang.String)">
<h3>withToken</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span className="element-name">withToken</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessToken)</span></div>
<div className="block"><p>SDK will pass access token as a Bearer.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>accessToken</code> - <p>Access token</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine"><code>AuthenticationMode</code></a> configured to use token</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withTokenProvider(com.here.sdk.core.engine.AuthenticationMode.AccessTokenProvider)">
<h3>withTokenProvider</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span className="element-name">withTokenProvider</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode-accesstokenprovider" title="interface in com.here.sdk.core.engine">AuthenticationMode.AccessTokenProvider</a> tokenProvider)</span></div>
<div className="block"><p>SDK will use access token provider to retrieve access token.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tokenProvider</code> - <p>Access token provider</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine"><code>AuthenticationMode</code></a> configured to use token provider</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withExternal()">
<h3>withExternal</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span className="element-name">withExternal</span>()</div>
<div className="block"><p>Assumes the authentication is provided by the client.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine"><code>AuthenticationMode</code></a> configured to use externally provided authentication</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withKeySecret(java.lang.String,java.lang.String)">
<h3>withKeySecret</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span className="element-name">withKeySecret</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessKeyId,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> accessKeySecret)</span></div>
<div className="block"><p>SDK will authenticate with access key id access key secret to obtain authentication token.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>accessKeyId</code> - <p>The access key id</p></dd>
<dd><code>accessKeySecret</code> - <p>The access key secret</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine"><code>AuthenticationMode</code></a> configured to use key ID and secret</p></dd>
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

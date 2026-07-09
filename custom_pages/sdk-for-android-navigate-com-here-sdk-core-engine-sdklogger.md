---
title: "SDKLogger (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-sdklogger"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SDKLogger.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.SDKLogger</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SDKLogger</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Logging interface for Android/iOS platforms.
 These logs are under management of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol" title="class in com.here.sdk.core.engine"><code>LogControl</code></a> and should be used instead of platform-specific logging functions.</p></div>
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
<section className="detail" id="log(com.here.sdk.core.engine.LogLevel,java.lang.String,java.lang.String)">
<h3>log</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">log</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>The severity of the log message.</p></dd>
<dd><code>tag</code> - <p>The log tag.</p></dd>
<dd><code>message</code> - <p>The log message.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="info(java.lang.String,java.lang.String)">
<h3>info</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">info</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div className="block"><p>convenient function to print a message with log level INFO and tag.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - <p>The log tag.</p></dd>
<dd><code>message</code> - <p>The log message.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="warn(java.lang.String,java.lang.String)">
<h3>warn</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">warn</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div className="block"><p>convenient function to print a message with log level WARNING and tag.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - <p>The log tag.</p></dd>
<dd><code>message</code> - <p>The log message.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="error(java.lang.String,java.lang.String)">
<h3>error</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">error</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div className="block"><p>convenient function to print a message with log level ERROR and tag.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - <p>The log tag.</p></dd>
<dd><code>message</code> - <p>The log message.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fatal(java.lang.String,java.lang.String)">
<h3>fatal</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">fatal</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div className="block"><p>convenient function to print a message with log level FATAL and tag.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - <p>The log tag.</p></dd>
<dd><code>message</code> - <p>The log message.</p></dd>
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

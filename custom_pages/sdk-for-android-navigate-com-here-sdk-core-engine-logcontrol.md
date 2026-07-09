---
title: "LogControl (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LogControl.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.LogControl</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LogControl</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This class provides functionality to enable/disable console logs as well as
 setting a custom log appender to receive log messages from the SDK. Note,
 this class will load native libraries of SDK, therefore generally it should be used
 just before SDK initialization, otherwise, it might have an unexpected performance
 impact if called not at the right time.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></code></div>
<div className="col-last even-row-color">
<div className="block">Invalid file path exception.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="enableLoggingToConsole(com.here.sdk.core.engine.LogLevel)">
<h3>enableLoggingToConsole</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">enableLoggingToConsole</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level)</span></div>
<div className="block"><p>Enables SDK logging messages to console that can be
 viewed using logcat tool.
 Enabled by default with <a href="sdk-for-android-navigate-loglevel#LOG_LEVEL_INFO"><code>LogLevel.LOG_LEVEL_INFO</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="disableLoggingToConsole()">
<h3>disableLoggingToConsole</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">disableLoggingToConsole</span>()</div>
<div className="block"><p>Disables SDK logging messages to console. Enabled by default with <a href="sdk-for-android-navigate-loglevel#LOG_LEVEL_INFO"><code>LogLevel.LOG_LEVEL_INFO</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="setAppender(com.here.sdk.core.engine.LogLevel,com.here.sdk.core.engine.LogAppender)">
<h3>setAppender</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setAppender</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logappender" title="interface in com.here.sdk.core.engine">LogAppender</a> appender)</span></div>
<div className="block"><p>Sets a custom log appender to receive log messages from the SDK.
 This overwrites a previous custom log appender set by user.
 Note, that setting the custom appender does not disable logging to the console made by SDK,
 in order to do that use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#disableLoggingToConsole()"><code>disableLoggingToConsole()</code></a> API.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
<dd><code>appender</code> - <p>New log appender.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setAppender(com.here.sdk.core.engine.LogLevel,java.lang.String)">
<h3>setAppender</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setAppender</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span>
                        throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></span></div>
<div className="block"><p>Sets a custom log appender that will write SDK log messages to a file.
 This overwrites a previous custom log appender set by user.
 Note, that setting the custom appender does not disable logging to the console made by SDK,
 in order to do that use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#disableLoggingToConsole()"><code>disableLoggingToConsole()</code></a> API.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
<dd><code>path</code> - <p>Absolute path to a file that the application has read/write permissions.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></code> - <p><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine"><code>LogControl.InvalidPathException</code></a> Indicates that the file path is invalid or not writeable.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAppender()">
<h3>removeAppender</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">removeAppender</span>()</div>
<div className="block"><p>Removes previously added custom log appender.</p></div>
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

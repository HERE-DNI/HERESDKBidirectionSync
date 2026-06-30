---
title: "LogControl (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LogControl.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.core.engine.LogControl</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LogControl</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This class provides functionality to enable/disable console logs as well as
 setting a custom log appender to receive log messages from the SDK. Note,
 this class will load native libraries of SDK, therefore generally it should be used
 just before SDK initialization, otherwise, it might have an unexpected performance
 impact if called not at the right time.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></code></div>
<div class="col-last even-row-color">
<div class="block">Invalid file path exception.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#disableLoggingToConsole()">disableLoggingToConsole</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disables SDK logging messages to console.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#enableLoggingToConsole(com.here.sdk.core.engine.LogLevel)">enableLoggingToConsole</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Enables SDK logging messages to console that can be
 viewed using logcat tool.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#removeAppender()">removeAppender</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes previously added custom log appender.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#setAppender(com.here.sdk.core.engine.LogLevel,com.here.sdk.core.engine.LogAppender)">setAppender</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logappender" title="interface in com.here.sdk.core.engine">LogAppender</a> appender)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets a custom log appender to receive log messages from the SDK.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#setAppender(com.here.sdk.core.engine.LogLevel,java.lang.String)">setAppender</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets a custom log appender that will write SDK log messages to a file.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="enableLoggingToConsole(com.here.sdk.core.engine.LogLevel)">
<h3>enableLoggingToConsole</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">enableLoggingToConsole</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level)</span></div>
<div class="block"><p>Enables SDK logging messages to console that can be
 viewed using logcat tool.
 Enabled by default with <a href="sdk-for-android-navigate-loglevel#LOG_LEVEL_INFO"><code>LogLevel.LOG_LEVEL_INFO</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disableLoggingToConsole()">
<h3>disableLoggingToConsole</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disableLoggingToConsole</span>()</div>
<div class="block"><p>Disables SDK logging messages to console. Enabled by default with <a href="sdk-for-android-navigate-loglevel#LOG_LEVEL_INFO"><code>LogLevel.LOG_LEVEL_INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="setAppender(com.here.sdk.core.engine.LogLevel,com.here.sdk.core.engine.LogAppender)">
<h3>setAppender</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAppender</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logappender" title="interface in com.here.sdk.core.engine">LogAppender</a> appender)</span></div>
<div class="block"><p>Sets a custom log appender to receive log messages from the SDK.
 This overwrites a previous custom log appender set by user.
 Note, that setting the custom appender does not disable logging to the console made by SDK,
 in order to do that use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#disableLoggingToConsole()"><code>disableLoggingToConsole()</code></a> API.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
<dd><code>appender</code> - <p>New log appender.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAppender(com.here.sdk.core.engine.LogLevel,java.lang.String)">
<h3>setAppender</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAppender</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a> level,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span>
                        throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></span></div>
<div class="block"><p>Sets a custom log appender that will write SDK log messages to a file.
 This overwrites a previous custom log appender set by user.
 Note, that setting the custom appender does not disable logging to the console made by SDK,
 in order to do that use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol#disableLoggingToConsole()"><code>disableLoggingToConsole()</code></a> API.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>level</code> - <p>Log level.</p></dd>
<dd><code>path</code> - <p>Absolute path to a file that the application has read/write permissions.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></code> - <p><a href="sdk-for-android-navigate-com-here-sdk-core-engine-logcontrol-invalidpathexception" title="class in com.here.sdk.core.engine"><code>LogControl.InvalidPathException</code></a> Indicates that the file path is invalid or not writeable.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAppender()">
<h3>removeAppender</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeAppender</span>()</div>
<div class="block"><p>Removes previously added custom log appender.</p></div>
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

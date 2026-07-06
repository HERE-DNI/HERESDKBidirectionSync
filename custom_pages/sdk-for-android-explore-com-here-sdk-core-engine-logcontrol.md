---
title: "LogControl (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-logcontrol"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.core.engine.LogControl →
com.here.NativeBase → com.here.sdk.core.engine.LogControl

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">LogControl</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

This class provides functionality to enable/disable console logs as well
as setting a custom log appender to receive log messages from the SDK.
Note, this class will load native libraries of SDK, therefore generally
it should be used just before SDK initialization, otherwise, it might
have an unexpected performance impact if called not at the right time.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception" class="type-name-link" title="class in com.here.sdk.core.engine"><code>LogControl.InvalidPathException</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Invalid file path exception.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      disableLoggingToConsole()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Disables SDK logging messages to console.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      enableLoggingToConsole(LogLevel level)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Enables SDK logging messages to console that can be viewed using
  logcat tool.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      removeAppender()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Removes previously added custom log appender.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setAppender(LogLevel level,
       LogAppender appender)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Sets a custom log appender to receive log messages from the SDK.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setAppender(LogLevel level,
       String path)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Sets a custom log appender that will write SDK log messages to a file.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-enableLoggingToConsole(com.here.sdk.core.engine.LogLevel)"
    class="section detail">

    ### enableLoggingToConsole

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">enableLoggingToConsole</span><span class="parameters">(@NonNull
    [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine") level)</span>

    </div>

    <div class="block">

    Enables SDK logging messages to console that can be viewed using
    logcat tool. Enabled by default with LogLevel.LOG_LEVEL_INFO .

    </div>

    Parameters:  
    `level` -

    Log level.

    </div>

  - <div id="sdk-for-android-explore-disableLoggingToConsole()"
    class="section detail">

    ### disableLoggingToConsole

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">disableLoggingToConsole</span>()

    </div>

    <div class="block">

    Disables SDK logging messages to console. Enabled by default with
    LogLevel.LOG_LEVEL_INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-setAppender(com.here.sdk.core.engine.LogLevel,com.here.sdk.core.engine.LogAppender)"
    class="section detail">

    ### setAppender

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setAppender</span><span class="parameters">(@NonNull
    [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine") level,
    @NonNull
    [LogAppender](sdk-for-android-explore-com-here-sdk-core-engine-logappender "interface in com.here.sdk.core.engine") appender)</span>

    </div>

    <div class="block">

    Sets a custom log appender to receive log messages from the SDK.
    This overwrites a previous custom log appender set by user. Note,
    that setting the custom appender does not disable logging to the
    console made by SDK, in order to do that use
    disableLoggingToConsole() API.

    </div>

    Parameters:  
    `level` -

    Log level.

    `appender` -

    New log appender.

    </div>

  - <div id="sdk-for-android-explore-setAppender(com.here.sdk.core.engine.LogLevel,java.lang.String)"
    class="section detail">

    ### setAppender

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setAppender</span><span class="parameters">(@NonNull
    [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine") level,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> path)</span>
    throws
    <span class="exceptions">[LogControl.InvalidPathException](sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception "class in com.here.sdk.core.engine")</span>

    </div>

    <div class="block">

    Sets a custom log appender that will write SDK log messages to a
    file. This overwrites a previous custom log appender set by user.
    Note, that setting the custom appender does not disable logging to
    the console made by SDK, in order to do that use
    disableLoggingToConsole() API.

    </div>

    Parameters:  
    `level` -

    Log level.

    `path` -

    Absolute path to a file that the application has read/write
    permissions.

    Throws:  
    [`LogControl.InvalidPathException`](sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception "class in com.here.sdk.core.engine")

    [`LogControl.InvalidPathException`](sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception "class in com.here.sdk.core.engine")
    Indicates that the file path is invalid or not writeable.

    </div>

  - <div id="sdk-for-android-explore-removeAppender()"
    class="section detail">

    ### removeAppender

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">removeAppender</span>()

    </div>

    <div class="block">

    Removes previously added custom log appender.

    </div>

    </div>

  </div>

</div>


---
title: "SDKLogger (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-sdklogger"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.core.engine.SDKLogger
→ com.here.NativeBase → com.here.sdk.core.engine.SDKLogger

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SDKLogger</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Logging interface for Android/iOS platforms. These logs are under
management of LogControl and should be used instead of platform-specific
logging functions.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>error(String tag,
   String message)</code></pre></td>
  <td><div class="block">
  convenient function to print a message with log level ERROR and tag.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>fatal(String tag,
   String message)</code></pre></td>
  <td><div class="block">
  convenient function to print a message with log level FATAL and tag.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>info(String tag,
   String message)</code></pre></td>
  <td><div class="block">
  convenient function to print a message with log level INFO and tag.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>log(LogLevel level,
   String tag,
   String message)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>warn(String tag,
   String message)</code></pre></td>
  <td><div class="block">
  convenient function to print a message with log level WARNING and tag.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="log(com.here.sdk.core.engine.LogLevel,java.lang.String,java.lang.String)"
    class="section detail">

    ### log

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">log</span><span class="parameters">(@NonNull
    [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine") level,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> tag,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    Parameters:  
    `level` -

    The severity of the log message.

    `tag` -

    The log tag.

    `message` -

    The log message.

    </div>

  - <div id="info(java.lang.String,java.lang.String)"
    class="section detail">

    ### info

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">info</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> tag,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    <div class="block">

    convenient function to print a message with log level INFO and tag.

    </div>

    Parameters:  
    `tag` -

    The log tag.

    `message` -

    The log message.

    </div>

  - <div id="warn(java.lang.String,java.lang.String)"
    class="section detail">

    ### warn

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">warn</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> tag,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    <div class="block">

    convenient function to print a message with log level WARNING and
    tag.

    </div>

    Parameters:  
    `tag` -

    The log tag.

    `message` -

    The log message.

    </div>

  - <div id="error(java.lang.String,java.lang.String)"
    class="section detail">

    ### error

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">error</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> tag,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    <div class="block">

    convenient function to print a message with log level ERROR and tag.

    </div>

    Parameters:  
    `tag` -

    The log tag.

    `message` -

    The log message.

    </div>

  - <div id="fatal(java.lang.String,java.lang.String)"
    class="section detail">

    ### fatal

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">fatal</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> tag,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    <div class="block">

    convenient function to print a message with log level FATAL and tag.

    </div>

    Parameters:  
    `tag` -

    The log tag.

    `message` -

    The log message.

    </div>

  </div>

</div>


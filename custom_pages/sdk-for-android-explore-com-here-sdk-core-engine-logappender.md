---
title: "LogAppender (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-logappender"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">LogAppender</span>

</div>

<div class="block">

An interface to implement a listener to receive log messages.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

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
  <td><code>void</code></td>
  <td><pre><code>log(LogLevel level,
   String message)</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="log(com.here.sdk.core.engine.LogLevel,java.lang.String)"
    class="section detail">

    ### log

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">log</span><span class="parameters">(@NonNull
    [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine") level,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> message)</span>

    </div>

    Parameters:  
    `level` -

    The severity of the log message.

    `message` -

    The log message.

    </div>

  </div>

</div>


---
title: "setCustomAppender method - LogControl class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-logcontrol-setcustomappender"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LogControl-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setCustomAppender</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setCustomAppender</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setCustomAppender-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setCustomAppender-param-appender" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-logappender-class">LogAppender</a></span> <span class="parameter-name">appender</span></span>

)

</div>

<div class="section desc markdown">

Sets a custom log appender to receive log messages from the SDK.

This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use <a href="sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole">LogControl.disableLoggingToConsole</a> API.

- `level` Log level.

- `appender` New log appender.

</div>

## Implementation

``` dart
static void setCustomAppender(LogLevel level, LogAppender appender) => $prototype.setCustomAppender(level, appender);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


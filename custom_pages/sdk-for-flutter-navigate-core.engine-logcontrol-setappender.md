---
title: "setAppender method - LogControl class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-logcontrol-setappender"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LogControl-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setAppender</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setAppender</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setAppender-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setAppender-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span></span>

)

</div>

<div class="section desc markdown">

Sets a custom log appender that will write SDK log messages to a file.

This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use <a href="sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole">LogControl.disableLoggingToConsole</a> API.

- `level` Log level.

- `path` Absolute path to a file that the application has read/write permissions.

Throws <a href="sdk-for-flutter-navigate-core-engine-logcontrolinvalidpathexceptionexception-class">LogControlInvalidPathExceptionException</a>. <a href="sdk-for-flutter-navigate-core-engine-logcontrolinvalidpathexceptionexception-class">LogControlInvalidPathExceptionException</a> Indicates that the file path is invalid or not writeable.

</div>

## Implementation

``` dart
static void setAppender(LogLevel level, String path) => $prototype.setAppender(level, path);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


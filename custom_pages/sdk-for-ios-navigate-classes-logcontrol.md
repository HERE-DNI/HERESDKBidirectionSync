---
title: "LogControl Class Reference"
slug: "sdk-for-ios-navigate-classes-logcontrol"
---

# LogControl

<div class="declaration">

<div class="language">

``` highlight
public class LogControl
```

``` highlight
extension LogControl: NativeBase
```

``` highlight
extension LogControl: Hashable
```

</div>

</div>

This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC16InvalidPathErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-InvalidPathError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC16InvalidPathErrora" class="token"><code>InvalidPathError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid file path exception.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InvalidPathError = String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC22enableLoggingToConsole5levelyAA0B5LevelO_tFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-enableLoggingToConsole-level" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC22enableLoggingToConsole5levelyAA0B5LevelO_tFZ" class="token"><code>enableLoggingToConsole(level:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables SDK logging messages to console that can be viewed using macOS Console app. Enabled by default with <a href="sdk-for-ios-navigate-enums-loglevel#sdk-for-ios-navigate-s-7heresdk8LogLevelO03logC4InfoyA2CmF">`LogLevel.logLevelInfo`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func enableLoggingToConsole(level: LogLevel)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-loglevel">LogLevel</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>level</code></em><code> </code></td>
  <td><div>
  <p>Log level.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC23disableLoggingToConsoleyyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-disableLoggingToConsole" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC23disableLoggingToConsoleyyFZ" class="token"><code>disableLoggingToConsole()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Disables SDK logging messages to console. Enabled by default with <a href="sdk-for-ios-navigate-enums-loglevel#sdk-for-ios-navigate-s-7heresdk8LogLevelO03logC4InfoyA2CmF">`LogLevel.logLevelInfo`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func disableLoggingToConsole()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC11setAppender5level8appenderyAA0B5LevelO_AA0bE0_ptFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setAppender-level-appender" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC11setAppender5level8appenderyAA0B5LevelO_AA0bE0_ptFZ" class="token"><code>setAppender(level:</code><wbr></wbr><code>appender:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom log appender to receive log messages from the SDK. This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC23disableLoggingToConsoleyyFZ">`LogControl.disableLoggingToConsole(...)`</a> API.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setAppender(level: LogLevel, appender: LogAppender)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-loglevel">LogLevel</a>
  - <a href="sdk-for-ios-navigate-protocols-logappender">LogAppender</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>level</code></em><code> </code></td>
  <td><div>
  <p>Log level.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>appender</code></em><code> </code></td>
  <td><div>
  <p>New log appender.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC11setAppender5level4pathyAA0B5LevelO_SStKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setAppender-level-path" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC11setAppender5level4pathyAA0B5LevelO_SStKFZ" class="token"><code>setAppender(level:</code><wbr></wbr><code>path:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom log appender that will write SDK log messages to a file. This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC23disableLoggingToConsoleyyFZ">`LogControl.disableLoggingToConsole(...)`</a> API.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC16InvalidPathErrora">`LogControl.InvalidPathError`</a> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC16InvalidPathErrora">`LogControl.InvalidPathError`</a> Indicates that the file path is invalid or not writeable.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setAppender(level: LogLevel, path: String) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-loglevel">LogLevel</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>level</code></em><code> </code></td>
  <td><div>
  <p>Log level.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>path</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to a file that the application has read/write permissions.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10LogControlC14removeAppenderyyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeAppender" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-logcontrol#sdk-for-ios-navigate-s-7heresdk10LogControlC14removeAppenderyyFZ" class="token"><code>removeAppender()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes previously added custom log appender.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func removeAppender()
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


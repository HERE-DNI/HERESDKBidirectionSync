---
title: "AssetsManager (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestassetsmanager"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AssetsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.AssetsManager
------------------------------------------------------------------------
public final class AssetsManager extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Assets manager interface. Can be used to make assets available to the SDK.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [AssetsManager](#%3Cinit%3E(com.here.sdk.mapview.MapContext))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context)`

Creates an instance of AssetsManager.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [registerFont](#registerFont(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` fontName, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` fontPath)`

Registers a font under a font name.

`void`

  [registerFontWithFallback](#registerFontWithFallback(java.lang.String,java.lang.String,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` fontName, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` fontPath, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> fallbackFontFilePaths)`

Registers a font set under a font name.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext)" class="section detail">

### AssetsManager

public AssetsManager(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context)

    Creates an instance of AssetsManager.
Parameters:
    `context` -

    MapContext to which the assets belong.

## Method Details

### registerFont

public void registerFont(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fontName, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fontPath)

    Registers a font under a font name. After registration, the font name can be used in

    - the SVG `text` tag as `font-family` attribute parameter when creating a [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") with `ImageFormat.SVG`.
    - [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

    Repeated registration with the same font name is ignored.
Parameters:
    `fontName` -

    A font name.

    `fontPath` -

    A font file path. TTF, OTF and WOFF formats are supported.

    Can be an asset file path or an absolute file path.

### registerFontWithFallback

public void registerFontWithFallback(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fontName, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fontPath, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> fallbackFontFilePaths)

    Registers a font set under a font name. After registration, the font name can be used in

    - the SVG `text` tag as `font-family` attribute parameter when creating a [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") with `ImageFormat.SVG`.
    - [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

    Repeated registration with the same font name is ignored.
Parameters:
    `fontName` -

    A font name.

    `fontPath` -

    A font file path. TTF, OTF and WOFF formats are supported.

    Can be an asset file path or an absolute file path.

    `fallbackFontFilePaths` -

    Additional font files are intended to be used if main font does not contain required character symbol and shall be sorted starting from most useful.

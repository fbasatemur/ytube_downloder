# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:37:59 2020

@author: fbasatemur
"""

from pytube import YouTube
import urllib.request


class Downloader():
      
      def __init__(self, url):
            self.URL = url
            self.itagList = []
            self.resList = []
            self.loadbarValue = 0
            self.fileSize = 0
            
      
      def dataInfo(self):
            self.ytStream = YouTube(self.URL) 
            self.thumbUrl = self.ytStream.thumbnail_url
            self.author = self.ytStream.author
            self.title = self.ytStream.title
            
      
      def downloadThumbImage(self):
            urllib.request.urlretrieve(self.thumbUrl, "thumbnail.jpg")
            
      def downloadInfoVideo(self):
            self.itagList.clear()
            self.resList.clear()
            self.streamsVideo = self.ytStream.streams.filter(file_extension = "mp4", progressive = True).all()
            
            for streams in self.streamsVideo:
                  self.itagList.append(streams.itag)
                  self.resList.append(streams.resolution)
      
      def downloadInfoAudio(self):
            self.itagList.clear()
            self.resList.clear()
            self.streamsAudio = self.ytStream.streams.filter(only_audio=True).all()
            
            for streams in self.streamsAudio:
                  self.itagList.append(streams.itag)
                  self.resList.append(streams.abr)
                  
      def download(self, itagNo):
            
            fileName = None
            if(len(self.title)):
                  fileName = self.title
                  
            selectStream = self.ytStream.streams.get_by_itag(itagNo)
            self.fileSize = selectStream.filesize
            selectStream.download(filename=fileName)
            
      

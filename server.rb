#!/usr/bin/ruby
require 'socket'

server = TCPServer.new 2000 # Server bound to port 2000

loop do
  client = server.accept    # Wait for a client to connect
  client.puts "Hello #{client.object_id}!"
  client.puts "Time is #{Time.now}"
  client.close
end